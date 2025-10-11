import asyncio
from common.logger import Logger
from peripherals.catalog.device_catalog import DeviceCatalog
from src.device_setup import DeviceSetup
from src.user_interface import UserInterface

logger = Logger.get_instance()

def main():
    logger.info(f'Starting IOT Hub')

    # Load configuration and peripherals
    catalog = load_configuration()  

    # Launch interactive menu in the main thread
    asyncio.run(UserInterface(catalog).main_menu())
    

def load_configuration() -> 'DeviceCatalog':
    catalog = DeviceSetup.initialize()
    print(f'Peripherals >> Communication Modules: [{len(catalog.communication_modules.all)}], Sensors: [{len(catalog.sensors.all)}], Actuators: [{len(catalog.actuators.all)}]. Total: [{len(catalog.peripherals)}]')

    return catalog

if __name__ == "__main__":
    main()
   




