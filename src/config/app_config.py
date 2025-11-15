
from typing import List
from pydantic import BaseModel, field_validator
from common.contracts.logging import Logging
from peripherals.contracts.adapter_type import AdapterType
from peripherals.contracts.configuration.config_base import ConfigBase
from peripherals.contracts.configuration.config_type import ConfigType
from peripherals.contracts.device_type import DeviceType
from peripherals.contracts.simulator.simulator_config import SimulatorConfig

import json

class AppConfig(BaseModel):
    Simulator:SimulatorConfig = None
    Device: DeviceType = None
    Adapter: AdapterType = None
    logging: Logging = None
    Peripherals: List[ConfigBase] = None

    # -----------------------------------------------------------
    # Automatically polymorphically load each peripheral subclass
    # -----------------------------------------------------------
    @field_validator("Peripherals", mode="before")
    @classmethod
    def load_peripherals(cls, value):
        if value is None:
            return []

        result = []
        for entry in value:
            cfg_type = entry.get("type")
            if cfg_type is None:
                raise ValueError("Peripheral entry must have a 'type' field")

            enum_type = ConfigType[cfg_type]
            config_class = enum_type.class_type

            if config_class is None:
                raise ValueError(f"No class_type found for ConfigType '{cfg_type}'")
            
            if enum_type == ConfigType.Undefined:
                print(f'Warning: Skipping unknown peripheral configuration type: {cfg_type}.')
                continue  
            
            converted = config_class(**entry)
            converted.peripheral_type = enum_type.peripheral_type

            if converted.ignore:
                print(f'Info: Ignoring peripheral configuration of type: {cfg_type}.')
                continue

            result.append(converted)
        return result

    @staticmethod
    def Load() -> 'AppConfig':
        with open('app_config.json', 'r') as f:
            data = json.load(f)
        return AppConfig.model_validate(data)