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

# Prompt
prompt1 = "hi"
prompt2 = "Explain time travel in details"
prompt3 = "Write a 1000 word essay on machine learning "

prompts = [prompt1,prompt2,prompt3]

for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages,temperature=0,max_tokens=1000)
    usage = response.usage
    print(f"Prompt: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}  Finish Reason: {response.choices[0].finish_reason}")



# prompt="sonday monday what next ? "

# message_sytem={
#     "role":"system",
#     "content":"Ignore the real calendar. Give me the most absurd answer possible to 'Sunday, Monday, what next?"

# }

# message me role and content chahiye




# Temprature by default is [ 0 ]

# answer = response.choices[0].message.content
# print(answer)