from typing import Optional
from pydantic import BaseModel

from peripherals.contracts.i2c_address import I2CAddress
from src.contracts.modules.i2c_multiplexer_reference_config import I2CMultiplexerReferenceConfig

class I2CBase(BaseModel):
    i2c_address: I2CAddress = I2CAddress.Unknown
    multiplexer: Optional[I2CMultiplexerReferenceConfig] = None