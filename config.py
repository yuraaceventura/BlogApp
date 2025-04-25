import pathlib

from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import BaseModel


BASE_DIR = pathlib.Path(__file__).parent.resolve()
env_file_path = BASE_DIR / '.env'

class SettingsBase(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file_path)


class DatabaseSettings(SettingsBase):
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: str

    def get_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class Settings(BaseModel):
    database: DatabaseSettings = DatabaseSettings()

settings = Settings()
