from typing import Any, Optional
from pydantic import BaseModel

from peripherals.communication.analog_digital_converter.adc_driver import ADCDriver

class ADCModuleReferenceConfig(BaseModel):
    name: str = None
    channel: int = None
    _adc:Optional[Any] = None

    @property
    def adc_module(self) -> 'ADCDriver':
        return self._adc

    def set_adc_module(self, adc_module: 'ADCDriver'):
        self._adc = adc_module