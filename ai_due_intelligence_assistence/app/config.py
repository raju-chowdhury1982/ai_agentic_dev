from dotenv import load_dotenv, find_dotenv
import os
from pydantic import BaseModel

# reading .env file
load_dotenv(find_dotenv())

# aoai_key = os.getenv("AZ_AOAI_KEY")
# model = os.getenv("AZ_MODEL")
# endpoint = os.getenv("AZ_ENDPOINT")
# api_version = os.getenv("API_VERSION")

# print(f"\nAOAI Key: {aoai_key}\nModel: {model}\nEndpoint: {endpoint}\nAPI Version: {api_version}")

class Settings(BaseModel):
    aoai_key: str
    model: str
    endpoint: str
    api_version: str

def get_settings() -> Settings:
    aoai_key = os.getenv("AZ_AOAI_KEY")
    model = os.getenv("AZ_MODEL")
    endpoint = os.getenv("AZ_ENDPOINT")
    api_version = os.getenv("API_VERSION")

    if not aoai_key:
        raise ValueError("OpenAI API Key is not found")
    if not model:
        raise ValueError("Model is not found")
    if not endpoint:
        raise ValueError("Endpoint is not found")
    if not api_version:
        raise ValueError("API Version is not found")
    return Settings(
        aoai_key=aoai_key, 
        model=model, 
        endpoint=endpoint, 
        api_version=api_version
        )

# if __name__ == "__main__":
#     settings = get_settings()
#     print(f"\nAOAI Key: {settings.aoai_key}\nModel: {settings.model}\nEndpoint: {settings.endpoint}\nAPI Version: {settings.api_version}")
