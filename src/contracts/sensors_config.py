from typing import List, Optional
from pydantic import BaseModel

from peripherals.sensors.temperature_sensors.config.config_base import TemperatureBaseConfig
from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.tds_sensors.config import TDSConfig

class SensorsConfig(BaseModel):
    TDSSensors: Optional[List[TDSConfig]] = None
    TemperatureSensors: Optional[List[TemperatureBaseConfig]] = None
    TemperatureSwitches: Optional[List[TempSwitchConfig]] = None