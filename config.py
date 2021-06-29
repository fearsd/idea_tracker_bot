"""Module gets config from env."""

from dotenv import dotenv_values

config = dotenv_values('.env')
