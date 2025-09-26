import time
from typing import Any, Optional
from common.environment import Env
from peripherals.actuators.action_decorator import ActionParam, coerce_input
from peripherals.actuators.actuator import Actuator
from peripherals.contracts.on_off_status import OnOffStatus
from peripherals.sensors.read_decorator import ReadAction
from peripherals.sensors.sensor import Sensor
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
                await self.sensor_selection_menu()
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
    

    async def sensor_selection_menu(self):
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

                    initialized = sensor.initialize()

                    if initialized:                    
                        Env.print(f"Initialized {sensor.name}...")
                        time.sleep(1)
                    else:
                        Env.print_paragraph(f"Failed to initialize {sensor.name}. Returning to main menu...","")
                        input("Press Enter to continue...")
                        continue

                    await self.sensor_action_menu(sensor)


                except (ValueError, IndexError):
                    Env.print("Invalid selection. Returning to main menu.")
                    return
                
    async def sensor_action_menu(self, sensor:Sensor):

        # If only one reading option, skip menu and monitor
        if (sensor.reading_options is None or len(sensor.reading_options) == 1):
            Env.clear_screan()
            Env.print(f"Only one reading option available. Starting monitoring of {sensor.name} every 3 seconds...")
            time.sleep(2)

            self.monitor_sensor(sensor, sensor.reading_options[0], 3)
            return

        while not self.completed:

            Env.clear_screan()
            Env.print_paragraph(f"<<<<<<<<< {sensor.name} Reading Options >>>>>>>>>", sensor, "")

            for i, action in enumerate(sensor.reading_options):
                print(f"{i + 1} - {action.label} ({action.description})")
            
            Env.print_paragraph(
                "-------------------------------",
                "B - Back to Sensor Selection",
                'X - Exit Application',
                ''
            )

            choice = input("Select an option: ").strip() 
            
            if choice.lower() == 'x':
                sensor.cleanup()
                self.completed = True
                
                Env.clear_screan()
                Env.print(f"Finished cleaning up {sensor.name}...")
                time.sleep(1)

                break      
            
            elif choice.lower() == 'b':
                sensor.cleanup()
                self.completed = True

                Env.clear_screan()
                Env.print(f"Finished cleaning up {sensor.name}...")
                time.sleep(1)

                break
            
            else:
                try:
                    idx = int(choice) - 1
                    action = sensor.reading_options[idx]

                    Env.clear_screan()
                    
                    # Prompt for parameters (if any)
                    args = self._prompt_for_params(action.params)

                    Env.print()
                    Env.print(f"Executing: {action.label}")

                    await self.monitor_sensor(sensor, action, 5, args)


                except (ValueError, IndexError):
                    Env.print("Invalid selection. Returning to previous menu.")
                    return
                except Exception as ex:
                    Env.print(f"Error executing action: {ex}")
                    input("Press Enter to continue...")


    def monitor_sensor(
        self,
        sensor: Sensor,
        reading_option: ReadAction,
        interval_seconds: int,
        args: Optional[dict[str, Any]] = None
    ):
        try:
            def read_callback(counter):
                result = reading_option.func(**args) if args else reading_option.func()
                readable_response = result.__str__() if hasattr(result, "__str__") else str(result)

                Env.clear_screan()
                Env.print_paragraph(
                    f"<<<<<<<<< Monitoring {sensor.name} >>>>>>>>>",
                    sensor,
                    f"Refresh Counter: {counter}",
                    "",
                    f"Result: {readable_response}", "", 
                    "<<<<< Press any key to stop monitoring >>>>>", ""
                )

            Env.monitor_until_keypress(read_callback, interval_seconds)

        except Exception as ex:
            Env.print(f"Error monitoring sensor [{sensor.name}] with action [{reading_option.label}]. Details: {ex}")
            input("Press Enter to continue...")




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
                        Env.print_paragraph(f"Failed to initialize {actuator.name}. Returning to main menu...","")
                        input("Press Enter to continue...")
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


