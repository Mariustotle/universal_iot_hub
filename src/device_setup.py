from typing import Any, List, Optional
from peripherals.catalog.device_catalog import DeviceCatalog

from common.logger import Logger
from peripherals.devices.device_base import DeviceBase
from src.config.app_config import AppConfig

logger = Logger.get_instance()

class DeviceSetup:

    @staticmethod
    def initialize(config:AppConfig, device:DeviceBase) -> DeviceCatalog:

        catalog = DeviceCatalog(
            is_simulated=config.Simulator.enabled, 
            device=device,
            device_type=config.Device,
            adapter_type=config.Adapter,
            peripherals=config.Peripherals) 

        return catalog


