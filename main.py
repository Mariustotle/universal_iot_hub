import asyncio
from common.logger import Logger
from src.device_setup import DeviceSetup
from src.peripheral_registry import PeripheralRegistry
from src.user_interface import UserInterface

logger = Logger.get_instance()

def main():
    logger.info(f'Starting IOT Hub')

    # Load configuration and peripherals
    registry = load_configuration()  

    # Launch interactive menu in the main thread
    asyncio.run(UserInterface(registry).main_menu())
    

def load_configuration() -> PeripheralRegistry:
    registry = DeviceSetup.initialize()
    print(f'Peripherals >> Communication Modules: [{len(registry.communication_modules)}], Sensors: [{len(registry.sensors)}], Actuators: [{len(registry.actuators)}]. Total: [{len(registry.peripherals)}]')

    return registry

if __name__ == "__main__":
    main()
   




