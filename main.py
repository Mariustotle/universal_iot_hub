from peripherals.actuators.relay_switches.relay_factory import RelayFactory
from peripherals.communication.i2c_expander.i2c_expander_factory import IOExpanderFactory
from peripherals.sensors.tds_sensors.tds_factory import TDSFactory

from common.logger import Logger
from src.device_setup import DeviceSetup

logger = Logger.get_instance()


def run():

    logger.info(f'Starting IOT Hub')
    registry = DeviceSetup.initialize()

    print(f'Total Peripherals: {len(registry.peripherals)}')
   

run()









