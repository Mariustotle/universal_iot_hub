from typing import List
from pydantic import BaseModel

from src.config.peripherals.sensors.tds_config_extension import TDSConfigExtension


class SensorsConfig(BaseModel):
    TDSSensors: List[TDSConfigExtension] = None