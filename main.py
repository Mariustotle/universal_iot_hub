import threading
from typing import Optional
from common.logger import Logger
from src.background_processes.background_process_base import BackgroundProcessBase
from src.background_processes.sensor_background_process import SensorBackgroundProcess
from src.device_setup import DeviceSetup
from src.peripheral_registry import PeripheralRegistry
from src.user_interface import UserInterface

logger = Logger.get_instance()


def start():
    logger.info(f'Starting IOT Hub')

    # Global cancellation event
    cancel_event = threading.Event()    

    # Load configuration and peripherals
    registry = load_configuration()  

    # Start background processes
    background = load_background_sensors(registry, cancel_event)

    # Launch interactive menu in the main thread
    UserInterface(registry).run_menu()

    # Stop across all threads
    cancel_event.set()      # poller will stop naturally
    background.join()       # wait until it finishes



def load_configuration() -> PeripheralRegistry:
    registry = DeviceSetup.initialize()
    print(f'Peripherals >> Communication Modules: [{len(registry.communication_modules)}], Sensors: [{len(registry.sensors)}], Actuators: [{len(registry.actuators)}]. Total: [{len(registry.peripherals)}]')

    return registry


def load_background_sensors(registry: PeripheralRegistry, cancel_event: Optional[threading.Event]) -> 'BackgroundProcessBase':
    process = SensorBackgroundProcess(
        registry=registry,
        interval_seconds=2,
        cancel_event=cancel_event
    )

    process.start()



start()
   




