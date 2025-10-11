from typing import List
from pydantic import BaseModel

from peripherals.communication.analog_digital_converter.config import ADCConfig
from peripherals.communication.i2c_multiplexer.config import I2CMultiplexerConfig


class CommunicationConfig(BaseModel):
    AnalogDigitalConverters: List[ADCConfig] = None
    I2CExpanders: List[I2CMultiplexerConfig] = None