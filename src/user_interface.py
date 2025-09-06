from src.peripheral_registry import PeripheralRegistry


class UserInterface:

    def __init__(self, registry: PeripheralRegistry):
        self.registry = registry

    def run_menu(self):
        while True:
            print("\n=== IOT Console Menu ===")
            print("1. View latest sensor data")
            print("2. Control an actuator")
            print("3. Exit")
            choice = input("Select an option: ").strip()

            if choice == "1":
                self.show_sensor_data()
            elif choice == "2":
                self.control_actuator()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid selection. Try again.")

    def show_sensor_data(self):
        with self.registry._lock:
            for sensor in self.registry.sensors:
                print(f"{sensor.name}: {sensor.latest_reading} (Last updated: {sensor.last_updated})")

    def control_actuator(self):
        with self.registry._lock:
            for i, actuator in enumerate(self.registry.actuators):
                print(f"{i + 1}. {actuator.name}")
        
        idx = int(input("Choose actuator to control: ")) - 1
        action = input("Enter 'on', 'off', or 'toggle': ").strip().lower()

        try:
            actuator = self.registry.actuators[idx]
            if action == 'on':
                actuator.switch_on()
            elif action == 'off':
                actuator.switch_off()
            elif action == 'toggle':
                actuator.toggle()
            else:
                print("Invalid action.")
        except Exception as e:
            print(f"Error controlling actuator: {e}")
