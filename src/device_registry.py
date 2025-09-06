from __future__ import annotations
from threading import RLock
from typing import Dict, List, Optional
from peripherals.actuators.actuator import Actuator

'''
Thread-safe registry for IoT Peripherals ( sensors, actuators, and displays)
'''
class DeviceRegistry:

    def __init__(self) -> None:
        self._lock = RLock()
        self._actuators: Dict[str, Actuator] = {}

    # Registration
    def register_actuator(self, actuator: Actuator) -> None:
        with self._lock:
            self._actuators[actuator.id] = actuator

    # Lookups
    def actuators(self) -> List[Actuator]:
        with self._lock:
            return list(self._actuators.values())


    def get_actuator(self, actuator_id: str) -> Optional[Actuator]:
        with self._lock:
            return self._actuators.get(actuator_id)

