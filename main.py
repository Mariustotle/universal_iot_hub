from peripherals.actuators.relay_switches.relay_factory import RelayFactory

from common.logger import Logger
from src.config.app_config import AppConfig
from src.device_registry import DeviceRegistry
logger = Logger.get_instance()


def run():

    logger.info(f'Starting IOT Hub')
    config = AppConfig.Load()
    register = DeviceRegistry()

    if config.Actuators.RelaySwitches is not None:

        for relay in config.Actuators.RelaySwitches:
            relay_device = RelayFactory.create(relay, config.Simulator)

            register.register_actuator(relay_device)

            logger.info(f'Registered device: {relay_device.get_description()}')

            # Switch ON
            relay_device.switch_on()

            # Switch OFF
            relay_device.switch_off()

            # Toggle
            relay_device.toggle()


run()









