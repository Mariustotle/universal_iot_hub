from typing import Any, Optional
from pydantic import BaseModel

from peripherals.communication.analog_digital_converter.adc_module import ADCModule

class ADCModuleReferenceConfig(BaseModel):
    name: str = None
    channel: int = None
    _adc:Optional[Any] = None

    @property
    def adc_module(self) -> 'ADCModule':
        return self._adc

    def set_adc_module(self, adc_module: 'ADCModule'):
        self._adc = adc_module