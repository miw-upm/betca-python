from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    ENVIRONMENT: str = Field(None, env="ENVIRONMENT")  # por default, 'env' is a environment var
    VAR: Optional[str]
    JWT_SECRET: Optional[str]

    class Config:
        env_file: str = "../config.env"


class DevSettings(Settings):
    class Config:
        env_prefix: str = "DEV_"


class ProdSettings(Settings):
    class Config:
        env_prefix: str = "PROD_"


def get_settings():
    if "prod" == Settings().ENVIRONMENT:
        return ProdSettings()
    else:
        return DevSettings()


config = get_settings()

print(config.ENVIRONMENT)
print(config.VAR)
print(config.JWT_SECRET)
