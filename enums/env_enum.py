import os
from enum import Enum

from dotenv import load_dotenv
load_dotenv()


class EnvEnum(Enum):    
    OPENAI_APIKEY = os.environ["OPENAI_APIKEY"]
