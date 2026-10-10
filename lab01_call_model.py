from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = "https://mohddashi-5792-resource.services.ai.azure.com/openai/v1"
deployment_name = "grok-4.6"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

completion = client.chat.completions.create(
    model=deployment_name,
   messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Question: What is Jordan"},
],

)

print(completion.choices[0].message.content)