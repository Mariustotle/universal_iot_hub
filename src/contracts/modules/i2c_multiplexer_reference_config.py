from typing import Any, Optional
from pydantic import BaseModel

from peripherals.communication.i2c_multiplexer.i2c_multiplexer import I2CMultiplexer

class I2CMultiplexerReferenceConfig(BaseModel):
    name: str = None
    channel: int = None
    _multiplexer:Optional[Any] = None

    @property
    def i2c_multiplexer(self) -> 'I2CMultiplexer':
        return self._multiplexer

    def set_multiplexer(self, multiplexer: 'I2CMultiplexer'):
        self._multiplexer = multiplexer

