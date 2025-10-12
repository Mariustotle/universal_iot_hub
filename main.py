import asyncio

from common.logger import Logger
from peripherals.catalog.device_catalog import DeviceCatalog
from src.splash_screen import SplashScreen
from src.device_setup import DeviceSetup
from src.user_interface import UserInterface
from common.environment import Env

logger = Logger.get_instance()


def main():
    logger.info(f'Starting IOT Hub')

    # Load configuration and peripherals
    catalog = load_configuration()  

    # Launch interactive menu in the main thread
    asyncio.run(UserInterface(catalog).main_menu())
    

def load_configuration() -> 'DeviceCatalog':

    Env.clear_screan()
    print('Loading configuration...')
    catalog = DeviceSetup.initialize()
    summary = catalog.get_device_configuration_summary()
    print('Configuration Loaded.')
    
    SplashScreen.display_configuration_summary(summary, 5)
    

    return catalog

if __name__ == "__main__":
    main()
   




