# 🌐 Universal IoT Hub

A modular, extensible IoT Hub built in Python for enthusiasts and developers to **prototype, test, and manage** various IoT peripherals.

## 📦 Resources

- [Project Home](https://github.com/Mariustotle/universal_iot_hub)
- 🚀[Setup and configure project](/docs/setup.md)
- 🔗 [Quick Refenerces](/docs/quick_references.md)
- [Debugging & Troubleshooting](/docs/debugging.md)


## 📦 Overview

- A shared peripheral catalog
  - Categorized by Sensors, Actuators, Display and communication modules
  - Driver extention, you can easily add more drivers to existing peripherals
- Use configuration to load dynamically from a shared catalog of peripherals
  - Can configure one or more instances of each type
  - Validate PIN and Module Dependancies at runtime
- Easily test and interact with sensors
  - Each peripheral have a simular mode so explore without peripherals
  - Interactive menu that dynamically shows available peripherals and interaction options

### Shared Peripheral Catalog
There is a referenced catelog of peripherals and their drivers that can be used across your IoT projects.

- [Index of available Peripherals](/peripherals/peripheral_index.md) - Naviage the available peripheral types
- [Portable submodule](https://github.com/Mariustotle/iot_peripherals) - Easy to use the underlying peripheral catalog in other projects, the underlying framework is in a diffferent repository than the example application.

### Configuration first approach


- **Simulator mode** - Use actual drivers and periphers or simulate them for testing
- **The type of device** e.g. Raspberry pi 3 which informs further validation and configuration options
- **Peripheral configurations** - What peripherals are attached?
  - **Sensors** - Peripherals that read values
  - **Actuators** - Peripherals that can cause change through actions
  - **Hybrid Peripherals** - Typically something that reads and then takes action if value is >, < or =
  - **Display modules** - Screens to show status and options
  - **Communication Modules** - Typically I2C Multiplexers or ADC Modules
    - **Connections** -These are dinamically created at runtime from references in other peripherals

```json
{
    "Simulator": true,
    "Device": "Raspberry Pi 3",
    "Sensors" : {
        "I2CComboSensors" :
        [
            {
                "name": "Workshop ENV Sensor",
                "driver": null,                
                "measurement": "Celsius",
                "i2c_address": "0x76",
                "multiplexer_details": {
                    "name": "I2C Extender",
                    "channel": 1
                }
            }
        ]
    },
    "Actuators" : {
        "RelaySwitches" : 
        [
            {
                "name": "Bedroom Light",
                "driver": "jqc3f_05vdc_c",
                "default_power_status": "Off",
                "gpio_pin": 12,
                "is_low_voltage_trigger": true,
                "use_direction_control": true
            }
        ]
    },
    "CommunicationModules": {
        "I2CMultiplexers": 
        [
            {
                "name": "I2C Extender",
                "multiplexer_address": "0x76",
                "number_of_channels": 8
            }
        ]
    }
}
```

The IoT Hub includes a splash screen to show the peripherals and warnings based on your configuration.
![Splash Screen](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/splash_screen.png)

**Highlights**
- Pin configuration might just look like an int but it can be extended to include GPIO/BOARD and labels
- Depending on the device type you might have onboard analog pins and I2C connections, the configurations allow you to specify either onboard or do it through ADC Converters or I2C Multiplexer modules

### Explore and interact
The main IoT Hub is an interactive console application, it does not have a specific business purpose other than the exploration and simulation of peripherals. The idea is that when you have a project idea you prototype the periphers here and then spin up a business specific version referencing the common Peripheral Catalog transfering your learnings.

![Interactive menu](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/interactive_console_menu.png)











