from typing import List
from pydantic import BaseModel
from peripherals.actuators.relay_switches.config import RelayConfig

class ActuatorsConfig(BaseModel):
    RelaySwitches: List[RelayConfig] = None