from typing import List
from pydantic import BaseModel
from peripherals.communication.analog_digital_converter.config import ADCConfig
from peripherals.communication.i2c_multiplexer.config import I2CMultiplexerConfig

class CommunicationsConfig(BaseModel):
    AnalogDigitalConverters: List[ADCConfig] = None
    I2CMultiplexers: List[I2CMultiplexerConfig] = None