# CLI-Based AI Project Agent

**Project Description:**  
This project is a **CLI-based AI Project Generator Agent**, inspired by Claude and GPT-style agents. It uses OpenAI’s Gemini API to generate **fully functional project folders and files** directly from user prompts. The agent runs entirely in the terminal and can automatically create frontend or backend project structures with working code.

---

## Features

- Generate **full project folders** with HTML, CSS, JS (frontend) or Python/Node.js (backend).  
- **Automatically writes all files** with complete code.  
- Works on **Windows terminals (CMD / PowerShell / VS Code Terminal)**.  
- Accepts user prompts like:  
  - `make calculator website`  
  - `create todo list app`  
  - `generate REST API project`  
- **Cross-functional CLI commands**: automatically runs commands to create folders, files, and open projects.  
- **Extensible**: can be adapted to other programming languages or frameworks.  

---

## Folder Structure

Example for a frontend project:

project-name/
│
├─ index.html # Main HTML file
├─ style.css # CSS file
├─ script.js # JavaScript file
├─ README.md # Project documentation
└─ other files # Any other files your AI agent generates



---

## Installation

1. **Clone or download** this repository:

```bash
git clone https://github.com/yourusername/cli-ai-agent.git
cd cli-ai-agent
