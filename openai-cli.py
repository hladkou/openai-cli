import sys
import openai
from termcolor import colored

openai.api_key = ""

if len(sys.argv) < 2:
   print("please provide a string argument")
   sys.exit(1)

input_string = sys.argv[1]

system_prompt = "you are an extremely helpful assistant"
user_prompt = input_string

messages = []
messages.append({"role": "system", "content": system_prompt})
messages.append({"role": "user", "content": user_prompt})

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=messages
)

completion_text = completion.choices[0].message.content
print(colored("\nChatGPT: ", "blue"), colored(completion_text, "blue"))

with open("conversation-log.txt", "a") as f:
    f.write(f"system_prompt: {system_prompt}\n\n")
    f.write(f"user_prompt: {user_prompt}\n\n")
    f.write(f"GPT: {completion_text}\n\n")
    f.write(f"*******************\n\n")
