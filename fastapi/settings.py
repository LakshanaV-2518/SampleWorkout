import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    def __init__(self):
        self.a = os.getenv('a')
        self.b = os.getenv('b')
        self.c = os.getenv('c')
        self.d = os.getenv('d')
        self.e = os.getenv('e')

    def get_all_attributes(self):
        return {key: value for key, value in self.__dict__.items() if value is not None}

    def get_attribute(self, key):
        return getattr(self, key, None)

# Create a settings instance to be used in the application
settings = Settings()
