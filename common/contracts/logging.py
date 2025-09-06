
from pydantic import BaseModel

class Logging(BaseModel):    
    file_name:str = None
    path:str = None
    level:str = None
    max_file_size_in_mb:int = None
    max_number_of_files:int = None