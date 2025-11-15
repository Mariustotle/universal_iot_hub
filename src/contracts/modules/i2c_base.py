from typing import Optional

from peripherals.contracts.configuration.config_base import ConfigBase
from peripherals.contracts.i2c_address import I2CAddress
from src.contracts.modules.i2c_multiplexer_reference_config import I2CMultiplexerReferenceConfig

class I2CBase(ConfigBase):
    i2c_address: I2CAddress = I2CAddress.Unknown
    multiplexer_details: Optional[I2CMultiplexerReferenceConfig] = None