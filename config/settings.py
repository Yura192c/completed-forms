from typing import Optional

from pydantic import MongoDsn
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class ConfigDatabase(BaseSettings):
    MONGODB_HOST: str = 'localhost'
    MONGODB_PORT: int = 27017

    MONGODB_NAME: str
    MONGODB_COLLECTION: str

    @property
    def database_url(self) -> Optional[MongoDsn]:
        return f"mongodb://{self.MONGODB_HOST}:{self.MONGODB_PORT}/"


settings_db = ConfigDatabase(_env_file="../.env", _env_file_encoding="utf-8")
