from typing import Any, Optional

from peripherals.communication.analog_digital_converter.adc_module import ADCModule
from peripherals.contracts.configuration.config_base import ConfigBase

class ADCModuleReferenceConfig(ConfigBase):
    name: str = None
    channel: int = None
    _adc:Optional[Any] = None

    @property
    def adc_module(self) -> 'ADCModule':
        return self._adc

    def set_adc_module(self, adc_module: 'ADCModule'):
        self._adc = adc_module