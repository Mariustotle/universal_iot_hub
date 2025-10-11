import asyncio
import time

from common.logger import Logger
from peripherals.catalog.device_catalog import DeviceCatalog
from peripherals.contracts.configuration_summary import ConfigurationSummary
from src.device_setup import DeviceSetup
from src.user_interface import UserInterface
from common.environment import Env

logger = Logger.get_instance()


def display_configuration_summary(summary: ConfigurationSummary) -> None:
    Env.clear_screan()
    Env.print_paragraph(
        f'Device: [{summary.device_type.value}] Configuration Summary',
        '------------------------------------------------',
        '')
    
    Env.print('>>> SENSORS <<<')
    for sensor in summary.sensors:
        Env.print(f'- {sensor.get_description()}')

    Env.print('\n>>> ACTUATORS <<<')
    for actuator in summary.actuators:
        Env.print(f'- {actuator.get_description()}')
    
    Env.print('\n>>> I2C MULTIPLEXERS <<<')
    for mux in summary.i2c_multiplexers:
        Env.print(f'- {mux.get_description()}')
        for conn in mux.connections:
            Env.print(f'   - {conn}')

    Env.print('\n>>> ADC MODULES <<<')
    for adc in summary.adc_modules:
        Env.print(f'- {adc.get_description()}')
        for conn in adc.connections:
            Env.print(f'   - {conn}')

    Env.print('\n>>> PIN Configuration <<<')
    for pin in summary.pin_configurations:
        Env.print(f'- {pin}')


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
    
    display_configuration_summary(summary)
    time.sleep(5)

    return catalog

if __name__ == "__main__":
    main()
   




