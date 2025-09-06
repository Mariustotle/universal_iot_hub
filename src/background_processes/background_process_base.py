import asyncio
import threading
import time
from abc import ABC, abstractmethod
from typing import Any, Optional

from src.peripheral_registry import PeripheralRegistry

class BackgroundProcessBase(ABC, threading.Thread):
    def __init__(
        self,
        registry: PeripheralRegistry,
        interval_seconds: float,
        name: Optional[str] = None,
        daemon: bool = True,
        run_immediately: bool = False,
        cancel_event: Optional[threading.Event] = None,
    ) -> None:
        super().__init__(name=name or self.__class__.__name__, daemon=daemon)
        if interval_seconds <= 0:
            raise ValueError("interval_seconds must be > 0")

        self.registry = registry
        self.interval = float(interval_seconds)
        self.run_immediately = run_immediately

        # Internal stop token (always exists)
        self._stop_evt = threading.Event()
        # Optional external token
        self._external_evt = cancel_event
        self._loop: Optional[asyncio.AbstractEventLoop] = None

    # ---------- To override ----------
    @abstractmethod
    async def run_cycle(self) -> None:
        raise NotImplementedError

    async def setup(self) -> None: ...
    async def teardown(self) -> None: ...

    # ---------- Control ----------
    def stop(self, timeout: Optional[float] = None) -> None:
        """Stop via internal token."""
        self._stop_evt.set()
        if self._loop and self._loop.is_running():
            self._loop.call_soon_threadsafe(lambda: None)
        self.join(timeout=timeout)

    def is_cancelled(self) -> bool:
        """Check both internal and external tokens."""
        return self._stop_evt.is_set() or (
            self._external_evt is not None and self._external_evt.is_set()
        )

    # ---------- Thread run ----------
    def run(self) -> None:
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        try:
            self._loop.run_until_complete(self._runner())
        finally:
            self._loop.close()

    async def _runner(self) -> None:
        await self.setup()
        try:
            next_run = time.monotonic()
            if self.run_immediately:
                await self._safe_run_cycle()
                next_run = time.monotonic()

            while not self.is_cancelled():
                next_run += self.interval
                await self._safe_run_cycle()

                delay = max(0.0, next_run - time.monotonic())
                await self._cooperative_sleep(delay)
        finally:
            await self.teardown()

    async def _cooperative_sleep(self, seconds: float) -> None:
        if seconds <= 0:
            return
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, lambda: self._stop_evt.wait(seconds))

    async def _safe_run_cycle(self) -> None:
        try:
            await self.run_cycle()
        except Exception as e:
            print(f"[{self.name}] run_cycle error: {e}")
