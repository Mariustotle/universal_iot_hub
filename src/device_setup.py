from typing import Any, List, Optional
from peripherals.catalog.device_catalog import DeviceCatalog
from src.config.app_config import AppConfig
from common.logger import Logger

logger = Logger.get_instance()

class DeviceSetup:

    @staticmethod
    def initialize() -> DeviceCatalog:
        config = AppConfig.Load()        

        sensors_config: Optional[List[Any]] = []
        actuators_config: Optional[List[Any]] = []
        communications_config: Optional[List[Any]] = []

        if config.CommunicationModules is not None:

            if config.CommunicationModules.I2CMultiplexers is not None:
                for expander in config.CommunicationModules.I2CMultiplexers:
                    communications_config.append(expander)                    

            if config.CommunicationModules.AnalogDigitalConverters is not None:
                for adc in config.CommunicationModules.AnalogDigitalConverters:
                    communications_config.append(adc)

        if config.Actuators is not None:
            if config.Actuators.RelaySwitches is not None:
                for relay in config.Actuators.RelaySwitches:
                    actuators_config.append(relay)

        if config.Sensors is not None:

            if config.Sensors.TDSSensors is not None:        
                for sensor_config in config.Sensors.TDSSensors:
                    sensors_config.append(sensor_config)

            if config.Sensors.TemperatureSwitches is not None:        
                for sensor_config in config.Sensors.TemperatureSwitches:
                    sensors_config.append(sensor_config)

            if config.Sensors.DigitalTemperatureSensors is not None:        
                for sensor_config in config.Sensors.DigitalTemperatureSensors:
                    sensors_config.append(sensor_config)

            if config.Sensors.I2CComboSensors is not None:        
                for sensor_config in config.Sensors.I2CComboSensors:
                    sensors_config.append(sensor_config)    


        catalog = DeviceCatalog(is_simulated=config.Simulator, 
            sensors_config=sensors_config,
            actuators_config=actuators_config,
            communications_config=communications_config) 

        return catalog


