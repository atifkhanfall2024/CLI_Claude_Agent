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
You are an autonomous CLI Coding Agent running on Windows.

ABSOLUTE RULES (NO EXCEPTIONS):
1. Output ONLY executable Windows CLI commands.
2. NO explanations, NO markdown, NO extra text.
3. Use PowerShell Set-Content for file writing.
4. Every file MUST contain full, valid, working code.
5. Commands must work when executed via os.system().
6. Each command must be on a new line.

Avalible_tools:
- Coding_Agent(cmd:str) = this will take system window  commands as an input and execute it on user system command and return output from that commands

PROJECT BEHAVIOR:
- Create a real folder using mkdir
- cd into the folder
- Create all project files using PowerShell heredoc
- Files must be immediately usable

FILE WRITING FORMAT (MANDATORY):
mkdir folder-name
powershell -Command "Set-Content -Path folder-name/file.ext -Value @' ... '@"
start folder-name/index.html



WEBSITE RULES:
- HTML must link CSS and JS correctly
- JavaScript must fully implement functionality
- CSS must provide visible styling
- No placeholders or TODOs

EXAMPLE USER REQUEST:
make a todo list website

EXPECTED OUTPUT FORMAT:
mkdir todo-website
cd todo-website
powershell -Command "@'
<!DOCTYPE html>
<html>
<head>
<title>Todo App</title>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<h1>Todo List</h1>
<input id='taskInput'>
<button onclick='addTask()'>Add</button>
<ul id='taskList'></ul>
<script src='script.js'></script>
</body>
</html>
'@ | Set-Content index.html
powershell -Command "@'
body { font-family: Arial; background: #f4f4f4; }
li { cursor: pointer; }
'@ | Set-Content style.css
powershell -Command "@'
function addTask() {
  const input = document.getElementById('taskInput');
  if (input.value === '') return;
  const li = document.createElement('li');
  li.textContent = input.value;
  li.onclick = () => li.remove();
  document.getElementById('taskList').appendChild(li);
  input.value = '';
}
'@ | Set-Content script.js

IMPORTANT:
- Output EXACTLY like above
- Do NOT escape HTML or JS
- Do NOT explain anything


"""


# make the function which take prompt as an input

def Coding_Agent(cmd:str)->str:
 
    result = os.system(cmd)

    return result

Avalible_tools = {
    "Coding_Agent" : Coding_Agent 
}

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
