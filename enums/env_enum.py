import os
from enum import Enum

from dotenv import load_dotenv
load_dotenv()


class EnvEnum(Enum):    
    DEFAULT_OPENAI_APIKEY = os.environ.get("DEFAULT_OPENAI_APIKEY", None)
