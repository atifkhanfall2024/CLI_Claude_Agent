from openai import OpenAI
from dotenv import load_dotenv
import os


# first i use openai sdk for calling gemini api 
load_dotenv()
key = os.getenv('GEMINI')

if not key:
    raise ValueError("Key is not present")

# using sdk of openai

client = OpenAI(
    api_key=key ,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# system prompt
System_Prompt_Template = """
You are a CLI-based coding assistant. Your work is to undestand user prompt carefully
1: you need to understand user prompt which he asked
2: paused for a second
3: then the response from llm have generated text 
4: then you need to make cli commands of it and run it automatically
5: make folder real time on the basis of commands
6: inside folder have fully functional files 

EXAMPLE 1:
User ask : todo list webiste prompt
. you need to take response from llm and automtically run cli based commands in window
. make real folder 
. folder like
. todo webiste
. inside it have files
. html with code
. css with code
. js with code 
. all are fully functional
"""


# make the function which take prompt as an input

def Coding_Agent(cmd:str):
 
    result = os.system(cmd)

    return result


def main():
    while True:
        user = input('>').strip()
        if user.lower() in ['exit' , 'quit']:
            print("Good Bye ")
            break

          # Get real weather
         

             

        response = client.chat.completions.create(
            model='gemini-2.5-flash',
            messages=[
                {"role":"system" , "content":System_Prompt_Template},
                {"role":"user" , "content":user}
            ]
        )

        print("\n" + response.choices[0].message.content + "\n")
        Coding_Agent(response.choices[0].message.content)
if __name__ == "__main__":
    main()
