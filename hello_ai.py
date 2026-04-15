# write first program to test Azure OpenAI connection
from azure.core.credentials import AzureKeyCredential
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from config import az_aoai_key

# Create an OpenAI client
chat_llm = AzureChatOpenAI(
    api_key=az_aoai_key,
    model="gpt-4o",
    azure_endpoint="https://starlink-openai-nprd.openai.azure.com/", 
    api_version="2024-05-01-preview"
)

messages = HumanMessage(content="Tell me a joke about Light bulbs.")

response = chat_llm.invoke([messages])

print(response.content)