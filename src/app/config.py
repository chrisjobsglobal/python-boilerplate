# src/app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    DATABASE_URL = "default_database_url"
    API_KEY = "default_api_key"

def get_config():
    environment = os.getenv("ENVIRONMENT", "development").lower()

    if environment == "production":
        config = Config()
        config.DEBUG = os.getenv("PROD_DEBUG", "False").lower() == "true"
        config.DATABASE_URL = os.getenv("PROD_DATABASE_URL", config.DATABASE_URL)
        config.API_KEY = os.getenv("PROD_API_KEY", config.API_KEY)
        return config

    elif environment == "testing":
        config = Config()
        config.DEBUG = os.getenv("TEST_DEBUG", "False").lower() == "true"
        config.DATABASE_URL = os.getenv("TEST_DATABASE_URL", config.DATABASE_URL)
        config.API_KEY = os.getenv("TEST_API_KEY", config.API_KEY)
        return config

    else: # development
        config = Config()
        config.DEBUG = os.getenv("DEV_DEBUG", "True").lower() == "true"
        config.DATABASE_URL = os.getenv("DEV_DATABASE_URL", config.DATABASE_URL)
        config.API_KEY = os.getenv("DEV_API_KEY", config.API_KEY)
        return config