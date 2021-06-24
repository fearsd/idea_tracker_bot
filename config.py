from dotenv import dotenv_values
import os

try:
    config = dotenv_values(".env")
except:
    config = os.environ