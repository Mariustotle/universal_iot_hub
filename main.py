




from peripherals.actuators.relay_switches.relay_config import RelayConfig
from peripherals.actuators.relay_switches.relay_driver_base import RelayDriverBase
from peripherals.actuators.relay_switches.relay_factory import RelayDevice, RelayFactory
from peripherals.actuators.relay_switches.relay_status import RelayStatus


def run():

    config:RelayConfig = RelayConfig(RelayStatus.Off, 9)
    relay_device:RelayDriverBase = RelayFactory.create(config, RelayDevice.JQC3F_05VDC_C)

    # Switch ON
    relay_device.switch_on()

    # Switch OFF
    relay_device.switch_off()

    # Toggle
    relay_device.toggle()


run()









