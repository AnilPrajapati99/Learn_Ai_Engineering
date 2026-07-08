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
prompt="sonday monday what next ? "

message_sytem={
    "role":"system",
    "content":"Ignore the real calendar. Give me the most absurd answer possible to 'Sunday, Monday, what next?"

}

# message me role and content chahiye

message={
    "role":role,
    "content":prompt
}

messages=[message_sytem, message]

# Temprature by default is [ 0 ]

response=client.chat.completions.create(model=model,messages=messages,temperature=0)
answer = response.choices[0].message.content
print(answer)