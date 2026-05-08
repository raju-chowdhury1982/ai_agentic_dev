from langchain_openai import AzureChatOpenAI

from app.config import get_settings


def get_chat_model(temperature: float = 0.01) -> AzureChatOpenAI:
    settings = get_settings()
    return AzureChatOpenAI(
        azure_endpoint=settings.endpoint,
        model=settings.model,
        api_version=settings.api_version,
        api_key=settings.aoai_key,  # type: ignore
        temperature=temperature,
    )
