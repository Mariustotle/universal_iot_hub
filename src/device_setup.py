from peripherals.actuators.relay_switches.factory import RelayFactory
from peripherals.communication.analog_digital_converter.adc_factory import ADCFactory
from peripherals.communication.i2c_expander.i2c_expander_factory import IOExpanderFactory
from peripherals.sensors.digital_temp_sensors.factory import DigitalTempFactory
from peripherals.sensors.tds_sensors.factory import TDSFactory
from src.peripheral_registry import PeripheralRegistry
from src.config.app_config import AppConfig
from common.logger import Logger

logger = Logger.get_instance()

class DeviceSetup:
    
    @staticmethod
    def initialize() -> PeripheralRegistry:

        config = AppConfig.Load()        
        registry = PeripheralRegistry()

        if config.CommunicationModules is not None:

            if config.CommunicationModules.I2CExpanders is not None:
                for expander in config.CommunicationModules.I2CExpanders:
                    expander_device = IOExpanderFactory.create(expander, config.Simulator)
                    registry.register_communication_module(expander_device)
                    logger.info(f'Registered device: {expander_device.get_description()}')

            if config.CommunicationModules.AnalogDigitalConverters is not None:
                for adc in config.CommunicationModules.AnalogDigitalConverters:
                    adc_device = ADCFactory.create(adc, config.Simulator)
                    registry.register_communication_module(adc_device)
                    logger.info(f'Registered device: {adc_device.get_description()}')

        if config.Actuators is not None:
            if config.Actuators.RelaySwitches is not None:
                for relay in config.Actuators.RelaySwitches:
                    relay_device = RelayFactory.create(relay, config.Simulator)
                    registry.register_actuator(relay_device)
                    logger.info(f'Registered device: {relay_device.get_description()}')

        if config.Sensors is not None:        

            if config.Sensors.TDSSensors is not None:        
                for tds in config.Sensors.TDSSensors:
                    tds_device = TDSFactory.create(tds, config.Simulator)
                    registry.register_sensor(tds_device)
                    logger.info(f'Registered device: {tds_device.get_description()}')


            if config.Sensors.DigitalTemperatureSensors is not None:        
                for digital_temp_config in config.Sensors.DigitalTemperatureSensors:
                    digital_temp = DigitalTempFactory.create(digital_temp_config, config.Simulator)
                    registry.register_sensor(digital_temp)
                    logger.info(f'Registered device: {digital_temp.get_description()}')

        return registry


