from typing import Optional

from peripherals.contracts.configuration.config_base import ConfigBase
from peripherals.contracts.i2c_address import I2CAddress
from peripherals.contracts.pins.pin_config import PinConfig
from src.contracts.modules.i2c_multiplexer_reference_config import I2CMultiplexerReferenceConfig

class I2CBase(ConfigBase):
    i2c_address: I2CAddress = I2CAddress.Unknown
    channel: int = None
    gpio_pin_sda:PinConfig = None
    gpio_pin_scl:PinConfig = None
    multiplexer_details: Optional[I2CMultiplexerReferenceConfig] = None