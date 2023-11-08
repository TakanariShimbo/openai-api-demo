import os
from enum import Enum

from dotenv import load_dotenv


class EnvEnum(Enum):
    load_dotenv()
    
    OPENAI_APIKEY = os.environ["OPENAI_APIKEY"]
