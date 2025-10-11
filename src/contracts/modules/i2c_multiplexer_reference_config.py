from typing import Any, Optional
from pydantic import BaseModel

from peripherals.communication.i2c_multiplexer.i2c_multiplexer_driver import I2CMultiplexerDriver

class I2CMultiplexerReferenceConfig(BaseModel):
    name: str = None
    channel: int = None
    _multiplexer:Optional[Any] = None

    @property
    def i2c_multiplexer(self) -> 'I2CMultiplexerDriver':
        return self._multiplexer

    def set_multiplexer(self, multiplexer: 'I2CMultiplexerDriver'):
        self._multiplexer = multiplexer

