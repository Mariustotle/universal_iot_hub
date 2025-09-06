
from pydantic import BaseModel
from typing import Optional
from common.config_reader import ConfigReader
from common.contracts.logging import Logging
from src.contracts.actuators_config import ActuatorsConfig

import json


class AppConfig(BaseModel):
    Simulator: bool = None
    logging: Logging = None
    Actuators: Optional[ActuatorsConfig] = None # type: ignore


    @staticmethod
    def Load() -> 'AppConfig':
        
        with open('app_config.json', 'r') as f:
                data = json.load(f)
        
        return AppConfig.model_validate(data)