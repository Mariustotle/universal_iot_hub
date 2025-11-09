
from pydantic import BaseModel
from typing import Optional
from common.contracts.logging import Logging
from peripherals.contracts.adapter_type import AdapterType
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.simulator.simulator_config import SimulatorConfig
from src.contracts.actuators_config import ActuatorsConfig
from src.contracts.communications_config import CommunicationsConfig
from src.contracts.sensors_config import SensorsConfig

import json

class AppConfig(BaseModel):
    Simulator:SimulatorConfig = None
    Device: DeviceType = None
    Adapter: AdapterType = None
    logging: Logging = None
    Actuators: Optional[ActuatorsConfig] = None
    Sensors: Optional[SensorsConfig] = None
    CommunicationModules: Optional[CommunicationsConfig] = None

    @staticmethod
    def Load() -> 'AppConfig':
        
        with open('app_config.json', 'r') as f:
                data = json.load(f)
        
        return AppConfig.model_validate(data)