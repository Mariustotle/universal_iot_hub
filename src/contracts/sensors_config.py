from typing import List, Optional
from pydantic import BaseModel

from peripherals.sensors.digital_temp_sensors.config import DigitalTempConfig
from peripherals.sensors.temperature_switch.config import TempSwitchConfig
from peripherals.sensors.tds_sensors.config import TDSConfig

class SensorsConfig(BaseModel):
    TDSSensors: Optional[List[TDSConfig]] = None
    DigitalTemperatureSensors: Optional[List[DigitalTempConfig]] = None
    TemperatureSwitches: Optional[List[TempSwitchConfig]] = None