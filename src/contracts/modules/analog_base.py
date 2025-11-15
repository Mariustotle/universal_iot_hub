from typing import Optional

from peripherals.contracts.configuration.config_base import ConfigBase
from peripherals.contracts.pins.pin_config import PinConfig
from src.contracts.modules.adc_module_reference_config import ADCModuleReferenceConfig

class AnalogBase(ConfigBase):
    gpio_pin: Optional[PinConfig] = None
    adc_details: Optional[ADCModuleReferenceConfig] = None