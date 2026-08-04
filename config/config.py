import os
from dotenv import load_dotenv

load_dotenv(override=True)

BASE_URL = os.getenv("APP_BASE_URL", "https://www.saucedemo.com")
APP_USERNAME = os.getenv("APP_USERNAME", "standard_user")
APP_PASSWORD = os.getenv("APP_PASSWORD", "secret_sauce")