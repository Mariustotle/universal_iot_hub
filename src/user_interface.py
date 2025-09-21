import time
from typing import Any
from common.environment import Env
from peripherals.actuators.action_decorator import ActionParam, coerce_input
from peripherals.actuators.actuator import Actuator
from peripherals.contracts.on_off_status import OnOffStatus
from src.peripheral_registry import PeripheralRegistry


class UserInterface:

    completed:bool = False

    def __init__(self, registry: PeripheralRegistry):
        self.registry = registry

    async def main_menu(self):
        while not self.completed:
            Env.clear_screan()
            Env.print_paragraph(
                "\n<<<<<<<<< Main Menu >>>>>>>>>",
                "",
                "1 - Read sensor (Get sensor reading)",
                "2 - Use actuator (Action something)",
                "-------------------------------",
                "X - Exit",
                ''
            )
            choice = input("Select an option: ").strip()            

            if choice == "1":
                await self.sensor_menu()
            elif choice == "2":
                await self.actuator_selection_menu()
            elif choice.lower() == "x":
                self.completed = True
                break
            else:
                print("Invalid selection. Try again.")
            
        Env.print("Exiting...")
        Env.print()

    def _prompt_for_params(self, params: list[ActionParam]) -> dict[str, Any]:
        if not params:
            return {}
        collected: dict[str, Any] = {}
        for p in params:
            # Enum choices pretty display
            hint = ""
            if p.choices:
                opts = list(p.choices)
                hint = f" Options: {opts}"
            elif isinstance(p.type_, type) and issubclass(p.type_, OnOffStatus):
                opts = [f"{i+1}:{m.name}" for i, m in enumerate(p.type_)]
                hint = f" [{', '.join(opts)}]"
            elif hasattr(p.type_, "__members__"):  # any Enum
                enum_cls = p.type_
                opts = [f"{i+1}:{m.name}" for i, m in enumerate(enum_cls)]
                hint = f" [{', '.join(opts)}]"

            default_txt = f" (default={p.default})" if not p.required and p.default is not None else ""
            prompt = f"Enter '{p.name}' ({p.type_.__name__}){hint}{default_txt}: "
            raw = input(prompt).strip()

            if raw == "" and not p.required:
                value = p.default
            else:
                value = coerce_input(raw, p.type_)
            collected[p.name] = value
        return collected

    async def sensor_menu(self):
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
                    reading = await sensor.read()
                    Env.print(reading.description)
                    Env.print()
                    input("Press Enter to continue...")

                except (ValueError, IndexError):
                    Env.print("Invalid selection. Returning to main menu.")
                    return


    async def actuator_selection_menu(self):
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
                    Env.clear_screan()

                    initialized = actuator.initialize()
                    if initialized:                    
                        Env.print(f"Initialized {actuator.name}...")
                        time.sleep(1)
                    else:
                        Env.print(f"Failed to initialize {actuator.name}. Returning to main menu...")
                        time.sleep(5)
                        continue

                    await self.actuator_action_menu(actuator)

                except (ValueError, IndexError):
                    Env.print("Invalid selection. Returning to main menu.")
                    return


    async def actuator_action_menu(self, actuator:Actuator):

        while not self.completed:

            Env.clear_screan()
            Env.print_paragraph(f"<<<<<<<<< {actuator.name} Available Actions >>>>>>>>>", actuator, "")

            for i, action in enumerate(actuator.actions):
                print(f"{i + 1} - {action.label} ({action.description})")
            
            Env.print_paragraph(
                "-------------------------------",
                "B - Back to Actuator Selection",
                'X - Exit Application',
                ''
            )

            choice = input("Select an option: ").strip() 
            
            if choice.lower() == 'x':
                actuator.cleanup()
                self.completed = True
                
                Env.clear_screan()
                Env.print(f"Finished cleaning up {actuator.name}...")
                time.sleep(1)

                break      
            
            elif choice.lower() == 'b':
                actuator.cleanup()
                self.completed = True

                Env.clear_screan()
                Env.print(f"Finished cleaning up {actuator.name}...")
                time.sleep(1)

                break
            
            else:
                try:
                    idx = int(choice) - 1
                    action = actuator.actions[idx]

                    Env.clear_screan()
                    
                    # Prompt for parameters (if any)
                    args = self._prompt_for_params(action.params)

                    Env.print()
                    Env.print(f"Executing: {action.label}")
                    # action.func is already a bound method; call with kwargs
                    result = action.func(**args) if args else action.func()

                    if (result != None):
                        Env.print(f"Result: {result}")
                    
                    Env.print_paragraph("", "New Status:", actuator)
                    
                    Env.print()
                    input("Press Enter to continue...")

                except (ValueError, IndexError):
                    Env.print("Invalid selection. Returning to previous menu.")
                    return
                except Exception as ex:
                    Env.print(f"Error executing action: {ex}")
                    input("Press Enter to continue...")


