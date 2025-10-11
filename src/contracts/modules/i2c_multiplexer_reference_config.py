from pydantic import BaseModel

class I2CMultiplexerReferenceConfig(BaseModel):
    name: str = None
    channel: int = None