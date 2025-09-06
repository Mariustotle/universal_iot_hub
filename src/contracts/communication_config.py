from typing import List
from pydantic import BaseModel

from peripherals.communication.analog_digital_converter.adc_config import ADCConfig
from peripherals.communication.i2c_expander.i2c_expander_config import I2CExpanderConfig


class CommunicationConfig(BaseModel):
    AnalogDigitalConverters: List[ADCConfig] = None
    I2CExpanders: List[I2CExpanderConfig] = None