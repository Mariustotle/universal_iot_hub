from common.environment import Env
from peripherals.actuators.actuator import Actuator
from src.peripheral_registry import PeripheralRegistry


class UserInterface:

    completed:bool = False

    def __init__(self, registry: PeripheralRegistry):
        self.registry = registry

    def main_menu(self):
        while not self.completed:
            Env.clear_screan()
            Env.print_paragraph(
                "\n<<<<<<<<< Main Menu >>>>>>>>>",
                "",
                "1 - View latest sensor data",
                "2 - Control an actuator",
                "-------------------------------",
                "X - Exit",
                ''
            )
            choice = input("Select an option: ").strip()            

            if choice == "1":
                self.sensor_menu()
            elif choice == "2":
                self.actuator_selection_menu()
            elif choice.lower() == "x":
                self.completed = True
                break
            else:
                print("Invalid selection. Try again.")
            
        Env.print("Exiting...")

    def sensor_menu(self):
        while not self.completed:

            Env.clear_screan()
            Env.print_paragraph("<<<<<<<<< Read Sensors >>>>>>>>>","")
            for i, sensor in enumerate(self.registry.sensors):
                print(f"{i + 1}. {sensor.name} [{sensor.sensor_type.name}]")
            
            Env.print_paragraph(
                "-------------------------------",
                "B - Back to Main Menu",
                'X - Exit Application',
                ''
            )

            choice = input("Select an option: ").strip() 
            
            if choice.lower() == 'x':
                self.completed = True      
                break      
            
            elif choice.lower() == 'b':
                break
            
            else:
                try:
                    idx = int(choice) - 1
                    sensor = self.registry.sensors[idx]
                    Env.clear_screan()

                    Env.print(f"Reading Sensor: {sensor.name} [{sensor.sensor_type.name}]")
                    reading = sensor.read()
                    Env.print(f"Latest Reading: >>>> {reading} <<<<")
                    Env.print()
                    input("Press Enter to continue...")

                except (ValueError, IndexError):
                    Env.print("Invalid selection. Returning to main menu.")
                    return


    def actuator_selection_menu(self):
        while not self.completed:

            Env.clear_screan()
            Env.print_paragraph("<<<<<<<<< Actuator Selection >>>>>>>>>","")
            for i, actuator in enumerate(self.registry.actuators):
                print(f"{i + 1}. {actuator.name} [{actuator.actuator_type.name}]")
            
            Env.print_paragraph(
                "-------------------------------",
                "B - Back to Main Menu",
                'X - Exit Application',
                ''
            )

            choice = input("Select an option: ").strip() 
            
            if choice.lower() == 'x':
                self.completed = True      
                break      
            
            elif choice.lower() == 'b':
                break
            
            else:
                try:
                    idx = int(choice) - 1
                    actuator = self.registry.actuators[idx]
                    self.actuator_action_menu(actuator)

                except (ValueError, IndexError):
                    Env.print("Invalid selection. Returning to main menu.")
                    return


    def actuator_action_menu(self, actuator:Actuator):
        while not self.completed:

            Env.clear_screan()
            Env.print_paragraph(f"<<<<<<<<< [{actuator.name}] Actions >>>>>>>>>","")

            for i, action in enumerate(actuator.actions):
                print(f"{i + 1} - {action.label} ({action.description})")
            
            Env.print_paragraph(
                "-------------------------------",
                "B - Back to Main Menu",
                'X - Exit Application',
                ''
            )

            choice = input("Select an option: ").strip() 
            
            if choice.lower() == 'x':
                self.completed = True      
                break      
            
            elif choice.lower() == 'b':
                break
            
            else:
                try:
                    idx = int(choice) - 1
                    action = actuator.actions[idx]
                    
                    # Request all parameters needed for action (One at a time)
                    # Take the action

                except (ValueError, IndexError):
                    Env.print("Invalid selection. Returning to main menu.")
                    return

