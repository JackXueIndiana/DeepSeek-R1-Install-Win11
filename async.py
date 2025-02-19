import asyncio
from ollama import AsyncClient

model = "deepseek-r1:1.5b"

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  response = await AsyncClient().chat(model=model, messages=[message])
  return response['message']['content']

resp = asyncio.run(chat())
print(resp)