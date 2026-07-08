import os
from pathlib import Path
from dotenv import load_dotenv                  
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Api Key Error")

client=Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role="user"
prompt="Who is Carryminati"

# message me role and content chahiye

message={
    "role":role,
    "content":prompt
}

messages=[message]

response=client.chat.completions.create(model=model,messages=messages)
# answer = response.choices[0].message.content
print(response)