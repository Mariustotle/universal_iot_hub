from typing import Optional

from peripherals.contracts.configuration.config_base import ConfigBase
from peripherals.contracts.pins.pin_config import PinConfig

class DigitalBase(ConfigBase):
    gpio_pin: Optional[PinConfig] = None