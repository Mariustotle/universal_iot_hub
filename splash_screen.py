from typing import Optional
from peripherals.contracts.configuration_summary import ConfigurationSummary
from common.environment import Env
import time

class SplashScreen:

    @staticmethod
    def display_configuration_summary(summary: ConfigurationSummary, delay_in_seconds: int) -> None:
        Env.clear_screan()

        fixed_width = 120  # Total box width including borders
        content_width = fixed_width - 4  # Space for content between '║' borders

        Env.print(f"{summary.device_type.value} Configuration Summary")

        def truncate(text: str, width: int) -> str:
            return text if len(text) <= width else text[:width - 3] + "..."

        def section_top(title: str, width: int = fixed_width, color: Optional[str] = None):
            Env.print(f"\n╔═ {title.upper()} " + '═' * (width - len(title) - 4), color)

        def section_bottom(width: int = fixed_width, color: Optional[str] = None):
            Env.print(f"╚" + '═' * (width - 2) + "╝", color)

        def print_boxed_lines(lines: list[str], width: int = fixed_width, color: Optional[str] = None):
            for line in lines:
                Env.print(f"║ {truncate(line, width - 4):<{width - 4}}", color)

               # ── Warnings
        if summary.warnings:
            warning_lines = [f"⚠  {w}" for w in summary.warnings]
            section_top("Configuration Warnings", color="red")

            # Use colored boxed lines
            for line in ["WARNING(S) DETECTED!", "-" * content_width] + warning_lines:
                Env.print(f"║ {truncate(line, content_width):<{content_width}}", color="red")

            section_bottom(color="red")
        else:
            section_top("Configuration Warnings", color="red")
            print_boxed_lines(["✓ No warnings detected."], color="red")
            section_bottom(color="red")

        # ── Sensors
        section_top("Sensors")
        for sensor in summary.sensors:
            Env.print(f"║ {truncate('• ' + sensor.get_description(), content_width):<{content_width}}")
        section_bottom()

        # ── Actuators
        section_top("Actuators")
        for actuator in summary.actuators:
            Env.print(f"║ {truncate('• ' + actuator.get_description(), content_width):<{content_width}}")
        section_bottom()

        # ── I2C Multiplexers
        section_top("I2C Multiplexers")
        for mux in summary.i2c_multiplexers:
            Env.print(f"║ {truncate('• ' + mux.get_description(), content_width):<{content_width}}")
            for conn in mux.connections:
                Env.print(f"║ {truncate('   ↳ ' + str(conn), content_width):<{content_width}}")
        section_bottom()

        # ── ADC Modules
        section_top("ADC Modules")
        for adc in summary.adc_modules:
            Env.print(f"║ {truncate('• ' + adc.get_description(), content_width):<{content_width}}")
            for conn in adc.connections:
                Env.print(f"║ {truncate('   ↳ ' + str(conn), content_width):<{content_width}}")
        section_bottom()

        # ── Pin Configuration
        section_top("Pin Configuration")
        for pin in summary.pin_configurations:
            Env.print(f"║ {truncate('• ' + str(pin), content_width):<{content_width}}")
        section_bottom()

        Env.print_paragraph('', '')
        time.sleep(delay_in_seconds)
