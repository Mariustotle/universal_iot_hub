from typing import Optional

from peripherals.contracts.configuration.config_base import ConfigBase
from peripherals.contracts.i2c_address import I2CAddress
from peripherals.contracts.pins.pin_config import PinConfig
from src.contracts.modules.i2c_multiplexer_reference_config import I2CMultiplexerReferenceConfig
from pydantic import BaseModel, field_validator, field_serializer

class I2CBase(ConfigBase):
    i2c_address: I2CAddress = I2CAddress.Unknown
    channel: int = None
    gpio_pin_sda:PinConfig = None
    gpio_pin_scl:PinConfig = None
    multiplexer_details: Optional[I2CMultiplexerReferenceConfig] = None


    @field_validator("i2c_address", mode="before")
    def parse_i2c_address(cls, v):
        # Already correct enum
        if isinstance(v, I2CAddress):
            return v

        # If string: could be name OR hex e.g. "0x38"
        if isinstance(v, str):
            # Try enum name first
            if v in I2CAddress.__members__:
                return I2CAddress[v]

            # Try hex literal
            if v.startswith("0x"):
                return I2CAddress(int(v, 16))

            # Try decimal string
            if v.isdigit():
                return I2CAddress(int(v))

            raise ValueError(f"Invalid I2CAddress '{v}'")

        # If int: direct conversion
        if isinstance(v, int):
            try:
                return I2CAddress(v)
            except ValueError:
                raise ValueError(f"Invalid I2C address value {v}")

        raise ValueError(f"Cannot parse I2CAddress from {v}")

    # ---------------------
    # OUTPUT SERIALIZATION
    # ---------------------
    @field_serializer("i2c_address", when_used="json")
    def serialize_i2c_address(self, v: I2CAddress):
        # Return the NAME not the integer
        return v.name