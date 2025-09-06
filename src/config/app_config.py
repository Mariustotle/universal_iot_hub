
from pydantic import BaseModel
from typing import Optional
from common.config_reader import ConfigReader
from common.contracts.logging import Logging
from src.contracts.actuators_config import ActuatorsConfig
from src.contracts.communication_config import CommunicationConfig
from src.contracts.sensors_config import SensorsConfig

import json

class AppConfig(BaseModel):
    Simulator: bool = None
    logging: Logging = None
    Actuators: Optional[ActuatorsConfig] = None
    Sensors: Optional[SensorsConfig] = None
    CommunicationModules: Optional[CommunicationConfig] = None

    @staticmethod
    def Load() -> 'AppConfig':
        
        with open('app_config.json', 'r') as f:
                data = json.load(f)
        
        return AppConfig.model_validate(data)