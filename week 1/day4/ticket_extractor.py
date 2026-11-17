import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Check your credentials")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"


class Ticket(BaseModel):
    name: str
    email: str
    issue: str


response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "ticket_extraction",
        "schema": Ticket.model_json_schema(),
    },
}

system_prompt = "Extract personal information and the support issue from the ticket."
text = "iam sultan from lahore email is abc@gmail.com phone number is 22342 my phone is broken"
prompt = f"Extract the specific information from: {text}"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt},
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0, 
    response_format=response_format,
)

raw_json = response.choices[0].message.content
ticket = Ticket.model_validate_json(raw_json)

print("Raw JSON:", raw_json)
print("Parsed Pydantic Object:", ticket)