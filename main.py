from peripherals.actuators.relay_switches.relay_factory import RelayFactory

from common.logger import Logger
from src.config.app_config import AppConfig
logger = Logger.get_instance()


def run():

    logger.info(f'Starting IOT Hub')
    config = AppConfig.Load()

    # config = RelayConfig.create(RelayStatus.Off, 9)

    if config.Actuators.RelaySwitches is not None:

        for relay in config.Actuators.RelaySwitches:
            relay_device = RelayFactory.create(relay, config.Simulator)

            # Switch ON
            relay_device.switch_on()

            # Switch OFF
            relay_device.switch_off()

            # Toggle
            relay_device.toggle()


run()









