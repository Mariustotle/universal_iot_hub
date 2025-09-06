from typing import List
from pydantic import BaseModel

from peripherals.sensors.tds_sensors.tds_config import TDSConfig

class SensorsConfig(BaseModel):
    TDSSensors: List[TDSConfig] = None