# AI Question-Answering Chatbot: Python Doubt Solver & Code Mentor

A terminal-based interactive chatbot built with **LangChain**, **Google Gemini API**, and **Rich**. It acts as an expert programming assistant, helping users resolve their Python programming doubts, debug errors, explain syntax, and learn optimization best practices.

## Features
- **LangChain Integration**: Utilizes modern LangChain architecture for model communication and prompt templating.
- **Google Gemini API**: Powered by the fast and capable `gemini-1.5-flash` model.
- **Premium Console UI**: Built with `rich` to render beautifully styled headers, interactive panel containers, live spinners during API generation, and formatted markdown output with syntax-highlighted Python code.
- **Robust Error Handling**: Safely handles missing API keys, network issues, and invalid credentials.

## Project Structure
```text
langchain_project/
 ├── .env                # Environment variables (API Key)
 ├── app.py              # Main application source code
 ├── requirements.txt    # Python dependencies
 └── README.md           # Project documentation
```

## Setup Instructions

### 1. Clone/Navigate to the Directory
Ensure you are in the project folder:
```bash
cd C:\Users\Shivananda\.gemini\antigravity-ide\scratch\langchain_project
```

### 2. Create and Activate Virtual Environment
Create a virtual environment:
```powershell
python -m venv .venv
```
Activate it:
- **PowerShell (Windows)**:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Command Prompt (Windows)**:
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
1. Obtain an API Key from [Google AI Studio](https://aistudio.google.com/).
2. Open the `.env` file.
3. Replace `YOUR_GEMINI_API_KEY` with your actual key:
   ```env
   GEMINI_API_KEY=AIzaSy...
   ```

## Running the Chatbot
Launch the chatbot:
```bash
python app.py
```

Type your Python doubts and press **Enter**. To exit the application, type `exit` or `quit`.

## Example Questions Tested
1. *What is the difference between list and tuple in Python?*
2. *How does a dictionary comprehension work? Explain with a simple example.*
3. *Why am I getting a NameError in this code: print(x)?*
4. *Write a Python function to check if a string is a palindrome.*
5. *Explain decorator pattern in Python with a real-world example.*
