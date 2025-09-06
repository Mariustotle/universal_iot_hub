from peripherals.actuators.relay_switches.relay_factory import RelayFactory

from common.logger import Logger
from src.config.app_config import AppConfig
logger = Logger.get_instance()


def run():

    logger.info(f'Starting IOT Hub')
    config = AppConfig.Load()

    if config.Actuators.RelaySwitches is not None:

        for relay in config.Actuators.RelaySwitches:
            relay_device = RelayFactory.create(relay, config.Simulator)

            logger.info(f'Registered device: {relay_device.get_description()}')

            # Switch ON
            relay_device.switch_on()

            # Switch OFF
            relay_device.switch_off()

            # Toggle
            relay_device.toggle()


run()









