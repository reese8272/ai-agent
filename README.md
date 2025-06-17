# 🧠 AI-Agent

An autonomous AI agent powered by the Gemini API. This system takes a user prompt, intelligently scans the codebase, selects valid functions, and iteratively attempts to complete the task until successful or until a maximum iteration limit is reached.

---

## 🚀 How It Works

1. You run the program via:

   ```bash
   python3 main.py "generate some code for me"
   ```
### The agent:
- Analyzes the working directory for files it is allowed to modify.
- Loads a list of predefined functions it is permitted to call.
- Uses the Gemini API to generate code and update files.
- Evaluates its own output, adjusts based on internal feedback, and retries if needed.

### The agent continues iterating until:
1. The task is marked as complete, or
2. It hits the maximum number of iterations.

## 🧩 Key Components
### File/Folder	Description
main.py	Entry point for the agent. Takes in your prompt and initiates the loop.
call_function.py	Handles execution and validation of allowed function calls.
prompts.py	Stores templates and system prompts for consistent agent guidance.
functions/	Modular task-specific functions the agent can invoke.
calculator/	An example submodule to show isolated function use.
config.py	Holds environment settings like API key, directories, and iteration limit.
tests.py	Basic unit tests to verify functionality.
requirements.txt	List of dependencies. Install via pip install -r requirements.txt.

## 🛠️ Installation
```bash
git clone https://github.com/reese8272/ai-agent.git
cd ai-agent
pip install -r requirements.txt
```
Make sure to set up your Gemini API key in config.py or as an environment variable.

## 🧪 Example Usage
```bash
python3 main.py "Write a function that reverses a string."
```

### The agent will:
- Search the functions/ folder for relevant tools
- Determine where to add or modify code
- Use Gemini to generate the solution
- Repeat the loop until the function passes a basic test or max iterations are hit

## 🧠 Agent Behavior
- Tool-aware: Only uses the functions you allow in the configuration
- File-aware: Only modifies files in allowed directories
- Self-correcting: Iterates intelligently using feedback from previous outputs
- Extensible: Easily add tools or modules in functions/ to expand capability

## 🧭 Future Improvements (WIP Ideas)
✅ Directory and function validation system
✅ Feedback loop and iteration control
🔄 Add LLM comparison support (e.g., OpenAI vs Gemini)
🔄 Enhanced error handling and logging
🔄 UI wrapper (FastAPI or CLI dashboard)

## 🤝 Contributions
Pull requests are welcome! You can:
Add new tools to the functions/ directory.
Improve the agent's reasoning or iteration logic.
Build additional prompts or refine prompts.py.

## 📜 License
MIT — open source, use freely.
