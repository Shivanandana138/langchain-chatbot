# 🤖 LangChain AI Python Assistant

An intelligent terminal-based AI chatbot built using **LangChain**, **Google Gemini API**, and **Rich**. This chatbot acts as a Python programming mentor by answering coding questions, explaining concepts, debugging errors, and generating clean Python solutions through an interactive command-line interface.

---

## 🚀 Features

- 🧠 Powered by **Google Gemini 1.5 Flash**
- 🔗 Built using **LangChain** for prompt management
- 🐍 Answers Python programming questions
- 🛠️ Debugs Python errors with detailed explanations
- 💡 Explains syntax and programming concepts in simple language
- ✨ Generates clean and optimized Python code
- 🎨 Beautiful terminal interface using **Rich**
- 📄 Markdown rendering with syntax-highlighted code
- 🔒 Secure API key management using `.env`
- ⚠️ Handles API and network errors gracefully

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangChain | LLM Framework |
| Google Gemini API | AI Language Model |
| Rich | Terminal User Interface |
| python-dotenv | Environment Variables |

---

## 📂 Project Structure

```text
langchain-chatbot/
│
├── app.py              # Main chatbot application
├── test_bot.py         # Testing file
├── requirements.txt    # Required dependencies
├── README.md           # Project documentation
├── .env.example        # Sample environment variables
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shivanandana138/langchain-chatbot.git

cd langchain-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

You can obtain a free API key from **Google AI Studio**.

---

## ▶️ Running the Chatbot

```bash
python app.py
```

Start asking your Python programming questions.

To exit the chatbot:

```text
exit
```

or

```text
quit
```

---

## 💬 Example Questions

- What is the difference between a list and a tuple?
- Explain Python decorators with an example.
- Why am I getting a NameError?
- Write a Python program to check for a palindrome.
- Explain dictionary comprehensions.
- How do generators work in Python?
- Optimize this Python function.

---

## 📸 Demo

> Add a screenshot or GIF of your chatbot here.

Example:

```markdown
![Demo](images/demo.png)
```

---

## 🎯 Future Improvements

- Conversation memory
- Multi-language programming support
- Streamlit/Web interface
- Voice input
- Chat history
- File upload support
- Multiple AI model support

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository, improve the project, and submit a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates further development.

---

## 👩‍💻 Author

**Shivanandana A**

GitHub: https://github.com/Shivanandana138

---

## 📄 License

This project is intended for educational and learning purposes.