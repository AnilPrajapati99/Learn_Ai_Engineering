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

# Structure it 
from pydantic import BaseModel

class Ticket(BaseModel):
    name:str
    email:str
    issue:str
    add:str
    phone:str

schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}
system_prompt=f"""
Extraxt the personal information from the ticket strictly based on the schema and give me the jsonformat output.{schema}
"""

message_system={
    "role":"system",
    "content":system_prompt
}


text="hello my name is Anil Prajapati , i have a Purachesed iphone to my girfriend nam is pinki but My batter is not Working , my addrese is Delhi , And my Phone no is 8780685597 and my email is anil@gmail.com"

# message_user={
#     "role":"user",
#     "content":text
# }


prompt=f"""
This is Customer Ticket,Please extract the personal inforamation from this.{text}
"""

# message me role and content chahiye

message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)
answer = response.choices[0].message.content
print(answer)

# Isko Padthe kaise hai 
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.add)
print(ticket.issue)
