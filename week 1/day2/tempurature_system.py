import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Check youe credientials")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"

messages = [
    #use system prompt
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "give me startup name for business regarding to clothing"}
]

response=client.chat.completions.create(model=model,messages=messages,temperature=1)
print(response.choices[0].message.content)
