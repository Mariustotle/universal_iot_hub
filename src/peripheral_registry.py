from __future__ import annotations
from threading import RLock
from typing import Dict, List, Optional
from peripherals.actuators.actuator import Actuator
from peripherals.communication.communication import Communication
from peripherals.peripheral import Peripheral
from peripherals.sensors.sensor import Sensor

'''
Thread-safe registry for IoT Peripherals ( sensors, actuators, and displays)
'''
class PeripheralRegistry:

    def __init__(self) -> None:
        self._lock = RLock()
        self._communication_modules: Dict[str, Communication] = {}
        self._actuators: Dict[str, Actuator] = {}
        self._sensors: Dict[str, Sensor] = {}

    @property
    def actuators(self) -> List[Actuator]:
        with self._lock:
            return list(self._actuators.values())
    
    @property
    def sensors(self) -> List[Sensor]:
        with self._lock:
            return list(self._sensors.values())
        
    @property
    def communication_modules(self) -> List[Communication]:
        with self._lock:
            return list(self._communication_modules.values())

    @property
    def peripherals(self) -> List[Peripheral]:
        with self._lock:
            combined: List[Peripheral] = (
                list(self._communication_modules.values())
                + list(self._actuators.values())
                + list(self._sensors.values())
            )
            return combined
        

    # Registration
    def register_communication_module(self, communication: Communication) -> None:
        with self._lock:
            self._communication_modules[communication.key] = communication

    def register_actuator(self, actuator: Actuator) -> None:
        with self._lock:
            self._actuators[actuator.key] = actuator

    def register_sensor(self, sensor: Sensor) -> None:
        with self._lock:
            self._sensors[sensor.key] = sensor

    # Lookups        
    def get_actuator(self, key: str) -> Optional[Actuator]:
        with self._lock:
            return self._actuators.get(key)
        
    def get_sensor(self, key: str) -> Optional[Sensor]:
        with self._lock:
            return self._sensors.get(key)        
        
    def get_communication_module(self, key: str) -> Optional[Communication]:
        with self._lock:
            return self._communication_modules.get(key)
        

