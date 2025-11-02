import asyncio

from common.logger import Logger
from peripherals.catalog.device_catalog import DeviceCatalog
from peripherals.devices.device_base import DeviceBase
from peripherals.devices.factory import DeviceFactory
from src.splash_screen import SplashScreen
from src.device_setup import DeviceSetup
from src.user_interface import UserInterface
from common.environment import Env
from src.config.app_config import AppConfig

logger = Logger.get_instance()

catelog:DeviceCatalog = None
device:DeviceBase = None


def main():
    logger.info(f'Starting IOT Hub')

    # Load configuration and peripherals
    catalog = load_configuration()

    # Launch interactive menu in the main thread
    asyncio.run(UserInterface(catalog=catalog).main_menu())
    

def load_configuration():

    Env.clear_screan()
    print('Loading configuration...')
    config = AppConfig.Load()

    print('Loading adapter...')
    device = DeviceFactory.create_device(config.Device, config.Adapter, config.Simulator)

    print('Setting up peripheral catalog')    
    catalog = DeviceSetup.initialize(config=config, device=device)

    summary = catalog.get_device_configuration_summary()
    print('Configuration Loaded.')
    
    SplashScreen.display_configuration_summary(summary, 5)

    return catalog

if __name__ == "__main__":
    main()
   




