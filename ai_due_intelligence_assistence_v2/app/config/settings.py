import os

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel

# reading env file
load_dotenv(find_dotenv())


class Settings(BaseModel):
    aoai_key: str
    model: str
    az_endpoint: str
    az_version: str


def get_settings() -> Settings:
    aoai_key = os.getenv("AZ_AOAI_KEY")
    model = os.getenv("AZ_MODEL")
    az_endpoint = os.getenv("AZ_ENDPOINT")
    az_version = os.getenv("API_VERSION")
    if not aoai_key:
        raise ValueError("OpenAI API Key is not found")
    if not model:
        raise ValueError("Model is not found")
    if not az_endpoint:
        raise ValueError("Endpoint is not found")
    if not az_version:
        raise ValueError("API Version is not found")
    return Settings(
        aoai_key=aoai_key, model=model, az_endpoint=az_endpoint, az_version=az_version  # type: ignore
    )


if __name__ == "__main__":
    conf = get_settings()

    print(conf.aoai_key)
    print(conf.model)
    print(conf.az_endpoint)
    print(conf.az_version)
