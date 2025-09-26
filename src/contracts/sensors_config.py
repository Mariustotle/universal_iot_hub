from typing import List
from pydantic import BaseModel

from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.tds_sensors.config import TDSConfig

class SensorsConfig(BaseModel):
    TDSSensors: List[TDSConfig] = None
    TemperatureSwitches: List[TempSwitchConfig] = None