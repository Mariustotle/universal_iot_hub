from typing import List
from pydantic import BaseModel

from peripherals.sensors.digital_temp_sensors.config import DigitalTempConfig
from peripherals.sensors.tds_sensors.config import TDSConfig

class SensorsConfig(BaseModel):
    TDSSensors: List[TDSConfig] = None
    DigitalTemperatureSensors: List[DigitalTempConfig] = None