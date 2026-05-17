from langchain_openai import AzureChatOpenAI

from app.config.settings import get_settings


def get_model(
    temperature: float = 0.1, max_tokens: int = 2048, top_p: float = 0.9
) -> AzureChatOpenAI:
    conf = get_settings()
    return AzureChatOpenAI(
        api_key=conf.aoai_key,
        api_version=conf.az_version,
        azure_endpoint=conf.az_endpoint,
        model=conf.model,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,  # type: ignore
    )
