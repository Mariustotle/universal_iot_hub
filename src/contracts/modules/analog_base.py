from typing import Optional
from pydantic import BaseModel

from src.contracts.modules.adc_module_reference_config import ADCModuleReferenceConfig

class AnalogBase(BaseModel):
    analog_pin: Optional[int] = None
    adc_details: Optional[ADCModuleReferenceConfig] = None