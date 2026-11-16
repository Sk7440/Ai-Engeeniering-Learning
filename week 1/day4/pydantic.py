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
prompt1="hi"
prompt2="explain anaomy in 100 word"
prompt3="write essay on money 1000 words"
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    messages = [
    #use system prompt
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
   ]
    response=client.chat.completions.create(model=model,messages=messages,temperature=1,max_tokens=100)
    usage=response.usage
    print(f"Prompt: {prompt} -->Your Tokens:{usage.prompt_tokens} completion_tokens:{usage.completion_tokens} total tokens: {usage.total_tokens} finish Reason:{response.choices[0].finish_reason}")





# messages = [
#     #use system prompt
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": prompt}
# ]

# response=client.chat.completions.create(model=model,messages=messages,temperature=1)
# print(response.choices[0].message.content)
