from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APP_NAME: str = ""
    APP_VERSION: str = ""
    OPENAI_API_KEY: str = ""

    FILE_ALLOWED_TYPES: list[str] = []
    FILE_MAX_SIZE: int = 0
    FILE_DEFAULT_CHUNK_SIZE: int = 0

def get_settings():
    return Settings()
