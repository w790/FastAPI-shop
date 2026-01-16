from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    app_name: str = "FastAPI Shop"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str) and not v.strip().startswith("["):
            return [i.strip() for i in v.split(",")]
        return v

    class Config:
        env_file = ".env"

settings = Settings()
