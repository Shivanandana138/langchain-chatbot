import os
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if hasattr(sys.stderr, 'reconfigure'):
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass
if hasattr(sys.stdin, 'reconfigure'):
    try:
        sys.stdin.reconfigure(encoding='utf-8')
    except Exception:
        pass

from dotenv import load_dotenv

load_dotenv()

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.text import Text
    from rich.prompt import Confirm
except ImportError:
    print("Error: The 'rich' library is required to run this application.")
    print("Please run: pip install rich")
    sys.exit(1)

console = Console()

DEMO_DATABASE = {
    "what is the difference between list and tuple in python?": """### Differences Between Lists and Tuples in Python

Both **lists** and **tuples** are sequence data types that can store collections of items, but they have key differences:

| Feature | List | Tuple |
| :--- | :--- | :--- |
| **Mutability** | **Mutable** (can be changed after creation). | **Immutable** (cannot be changed after creation). |
| **Syntax** | Defined with square brackets: `[1, 2, 3]` | Defined with parentheses: `(1, 2, 3)` |
| **Performance** | Slower (requires more memory allocation). | Faster (fixed size, optimized read-only memory). |
| **Use Case** | For data that needs to be modified dynamically. | For constant/static data that shouldn't change. |

#### Example:
```python
# List Example (Mutable)
my_list = [1, 2, 3]
my_list[0] = 99  # Works! my_list is now [99, 2, 3]

# Tuple Example (Immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 99  # Throws a TypeError!
```""",
    "how does a dictionary comprehension work? explain with a simple example.": """### Dictionary Comprehensions in Python

A **dictionary comprehension** is a concise, elegant way to create dictionaries in Python using an iterable. It is similar to list comprehensions but uses key-value syntax `{key: value}`.

#### Syntax:
```python
{key_expression: value_expression for item in iterable if condition}
```

#### Simple Example:
Let's create a dictionary mapping numbers to their squares:

```python
# Creating a dictionary of squares for numbers 1 to 5
squares = {num: num**2 for num in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### Filtering Example:
You can also include an `if` condition. Let's square only the even numbers:
```python
even_squares = {num: num**2 for num in range(1, 6) if num % 2 == 0}
print(even_squares)
# Output: {2: 4, 4: 16}
```""",
    "why am I getting a NameError in this code: print(x)?": """### Troubleshooting: `NameError: name 'x' is not defined`

A `NameError` in Python occurs when the interpreter tries to access or evaluate a variable name that has not been defined or assigned a value in the current scope.

#### Why it happened:
In your code `print(x)`, Python does not know what `x` refers to because it hasn't been declared yet.

#### How to fix it:
1. **Assign a value to the variable** before using or printing it:
   ```python
   x = 10  # Define x first
   print(x)  # Now it works!
   ```
2. **Check for typos**: Ensure the variable is spelled exactly the same way (Python is case-sensitive):
   ```python
   my_variable = "Hello"
   # print(my_var)  # Error: 'my_var' is not defined
   print(my_variable)  # Correct!
   ```
3. **Check scope**: If the variable was defined inside a function, it cannot be accessed outside that function:
   ```python
   def my_func():
       y = 5
   my_func()
   # print(y)  # Error: y is only available inside my_func
   ```""",
    "write a python function to check if a string is a palindrome.": """### Python Palindrome Checker

A string is a **palindrome** if it reads the same forward and backward (e.g., "radar", "level", "madam").

Here is an elegant Python function to check for palindromes, handling case sensitivity and spaces:

```python
def is_palindrome(text: str) -> bool:
    # 1. Convert to lowercase and remove spaces/non-alphanumeric characters
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    
    # 2. Check if the string matches its reverse
    return cleaned_text == cleaned_text[::-1]

# --- Testing the function ---
print(is_palindrome("racecar"))  # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))    # False
```

#### How it works:
- `char.isalnum()` strips away spaces and punctuation.
- `cleaned_text[::-1]` uses Python's slicing syntax to reverse the string.
- Comparing `cleaned_text` with its slice reverse returns `True` if they are identical.""",
    "explain decorator pattern in python with a real-world example.": """### Decorators in Python

A **decorator** is a design pattern in Python that allows you to modify or extend the behavior of a function or class without permanently modifying its source code. They are highly useful for tasks like logging, authentication, and execution timing.

Under the hood, a decorator is a function that takes another function as an argument, adds some functionality, and returns a new function.

#### Real-World Example: Logging Function Execution Time
Here is how to create a decorator that measures how long a function takes to run:

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"[Timer] Function '{func.__name__}' took {execution_time:.6f} seconds to run.")
        return result
    return wrapper

# Using the decorator with the @ symbol
@timer_decorator
def calculate_heavy_sum(limit):
    return sum(i for i in range(limit))

# Call the decorated function
calculate_heavy_sum(10000000)
# Output:
# [Timer] Function 'calculate_heavy_sum' took 0.452132 seconds to run.
```

#### Key Concepts:
- **`wrapper(*args, **kwargs)`**: The inner function that wraps the original. Using `*args` and `**kwargs` allows the decorator to be applied to functions with any arguments.
- **`@timer_decorator`**: The syntactic sugar in Python to apply the decorator."""
}

def get_demo_response(question):
    """Provide a helpful response for common Python questions in Demo Mode."""
    cleaned_q = question.strip().lower()
    cleaned_q = "".join(ch for ch in cleaned_q if ch.isalnum() or ch.isspace())

    for key, value in DEMO_DATABASE.items():
        cleaned_key = key.lower().replace("?", "").replace(".", "")
        if cleaned_q == cleaned_key or cleaned_q in cleaned_key or cleaned_key in cleaned_q:
            return value

    if "string" in cleaned_q:
        return """### Strings in Python

A string is a sequence of characters used to store text. In Python, strings are created with single or double quotes:

```python
name = \"Alice\"
message = 'Hello, world!'
```

Strings support operations like concatenation, slicing, and formatting. For example:

```python
full_name = name + \" Smith\"
print(full_name)
```"""

    if "list" in cleaned_q and "tuple" in cleaned_q or "difference" in cleaned_q and ("list" in cleaned_q or "tuple" in cleaned_q):
        return """### Lists vs Tuples

Lists are mutable, which means you can change their contents after creation. Tuples are immutable, so they cannot be changed once created.

```python
numbers = [1, 2, 3]   # list
numbers.append(4)    # allowed

coords = (10, 20)     # tuple
# coords[0] = 15      # would raise an error
```"""

    if "dictionary" in cleaned_q and "comprehension" in cleaned_q:
        return """### Dictionary Comprehensions

A dictionary comprehension creates a dictionary in a compact way using a single expression.

```python
squares = {x: x * x for x in range(1, 6)}
print(squares)
```

This builds the same result as a loop, but in a shorter syntax."""

    if "nameerror" in cleaned_q or "name error" in cleaned_q:
        return """### NameError

A NameError happens when Python tries to use a variable that has not been defined yet.

```python
print(x)  # x was never assigned
```

Fix it by assigning a value before using the variable:

```python
x = 10
print(x)
```"""

    if "palindrome" in cleaned_q:
        return """### Palindrome Checker

A palindrome reads the same forward and backward.

```python
def is_palindrome(text: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
```

Example:

```python
print(is_palindrome("racecar"))
```"""

    if "decorator" in cleaned_q:
        return """### Decorators

A decorator lets you wrap a function with extra behavior, such as logging or timing.

```python
def greet(name):
    return f"Hello, {name}"


def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)
    return wrapper

logged_greet = log_call(greet)
print(logged_greet("Ada"))
```"""

    if "function" in cleaned_q:
        return """### Functions in Python

A function is a reusable block of code that performs a specific task.

```python
def add(a, b):
    return a + b

print(add(2, 3))
```"""

    if "loop" in cleaned_q:
        return """### Loops in Python

Loops let you repeat a block of code multiple times.

```python
for i in range(3):
    print(i)
```"""

    if "class" in cleaned_q or "object" in cleaned_q:
        return """### Classes and Objects

A class defines a blueprint, while an object is an instance of that class.

```python
class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Bruno")
print(my_dog.name)
```"""

    return f"""### Demo Mode Response

You asked: *"{question}"*

*(Note: The chatbot is currently running in **Demo Mode** because a valid Gemini API Key was not found in the `.env` file.)*

Here is a helpful Python-focused answer:

- Break the problem into smaller parts.
- Write a minimal example to reproduce the issue.
- Use clear variable names and test your code step by step.

If you want, I can help you with a specific Python topic such as strings, lists, dictionaries, functions, classes, or debugging errors."""

def check_environment():
    """Check whether a Gemini API key is configured."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key.strip() == "" or api_key == "YOUR_GEMINI_API_KEY":
        console.print(Panel(
            Text.assemble(
                ("Warning: GEMINI_API_KEY is not configured!\n\n", "bold yellow"),
                ("Please follow these steps to set it up for live AI responses:\n", "white"),
                ("1. Get a free API Key from Google AI Studio (https://aistudio.google.com/)\n", "cyan"),
                ("2. Open the ", "white"),
                (".env", "bold cyan"),
                (" file in the project folder\n", "white"),
                ("3. Set ", "white"),
                ("GEMINI_API_KEY=your_actual_api_key_here\n", "bold green"),
                ("4. Restart this application.\n\n", "white"),
                ("Would you like to run in ", "white"),
                ("Demo Mode", "bold green"),
                (" to test the console interface and pre-configured doubts?", "white")
            ),
            title="[bold yellow]API Key Not Configured[/]",
            border_style="yellow"
        ))
        
        try:
            choice = Confirm.ask("Launch Demo Mode?", default=True)
            if choice:
                console.print("\n[bold green]Starting in Demo Mode... (No API Key required)[/]\n")
                return None
            else:
                sys.exit(1)
        except Exception:
            console.print("[bold red]Non-interactive environment detected. Exiting...[/]")
            sys.exit(1)

    return api_key

api_key = check_environment()
demo_mode = (api_key is None)

if not demo_mode:
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import StrOutputParser
    except ImportError as e:
        console.print(Panel(
            f"[bold red]Import Error:[/] Required dependencies are missing.\n"
            f"Missing package info: {str(e)}\n\n"
            f"Please run: [bold green]pip install langchain langchain-google-genai python-dotenv[/]",
            title="[bold red]Missing Dependencies[/]",
            border_style="red"
        ))
        sys.exit(1)

def build_solver_chain():
    """Build the LangChain pipeline."""
    system_instruction = (
        "You are an expert, friendly Python Doubt Solver & Code Mentor. "
        "Your mission is to help users resolve Python programming doubts, "
        "explain Python concepts, debug syntax or runtime errors, and write clean, optimized code.\n\n"
        "Please follow these guidelines:\n"
        "1. Keep explanations clear, well-structured, and concise.\n"
        "2. Always format Python code inside markdown blocks with syntax highlighting (e.g. ```python ... ```).\n"
        "3. Provide step-by-step guidance when debugging code.\n"
        "4. If a question is entirely unrelated to Python or programming, politely explain that your expertise "
        "is focused on Python doubt solving and ask how you can help with programming.\n"
        "5. Provide illustrative, simple code examples to clarify your explanations."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_instruction),
        ("human", "{question}")
    ])

    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        google_api_key=api_key
    )

    chain = prompt | model | StrOutputParser()
    return chain

def main():
    mode_text = "Demo Mode" if demo_mode else "Live Gemini AI Mode"
    mode_style = "bold yellow" if demo_mode else "bold green"
    
    console.print(Panel(
        Text.assemble(
            ("🐍 Python Doubt Solver & Code Mentor 🐍\n", "bold green"),
            ("Powered by LangChain & Google Gemini 1.5 Flash\n", "italic dark_green"),
            ("Current Status: ", "white"),
            (mode_text, mode_style),
            ("\n\nAsk questions about syntax, error messages, code logic, or optimization.\n", "white"),
            ("Type ", "white"),
            ("exit", "bold yellow"),
            (" or ", "white"),
            ("quit", "bold yellow"),
            (" to close the program.", "white")
        ),
        title="[bold green]Welcome[/]",
        border_style="green",
        expand=False
    ))
    console.print()

    chain = None
    if not demo_mode:
        try:
            chain = build_solver_chain()
        except Exception as e:
            console.print(f"[bold red]Initialization Error:[/] Failed to build LangChain pipeline. Details: {e}")
            sys.exit(1)

    while True:
        try:
            question = console.input("[bold cyan]Question >>> [/]").strip()
            
            if not question:
                continue
            if question.lower() in ("exit", "quit"):
                console.print("\n[bold green]Happy coding! Goodbye! 🐍[/]")
                break
            
            console.print()
            
            if demo_mode:
                with console.status("[bold blue]Demo Mentor is reviewing the code...[/]", spinner="dots"):
                    time.sleep(1.2)
                answer = get_demo_response(question)
            else:
                with console.status("[bold blue]Mentor is thinking...[/]", spinner="dots"):
                    answer = chain.invoke({"question": question})
            
            console.print(Panel(
                Markdown(answer),
                title="[bold green]Mentor's Explanation[/]",
                border_style="green",
                padding=(1, 2)
            ))
            console.print()
            
        except KeyboardInterrupt:
            console.print("\n\n[bold green]Happy coding! Goodbye! 🐍[/]")
            break
        except Exception as e:
            console.print(Panel(
                f"[bold red]Error:[/] {str(e)}",
                title="[bold red]Application Error[/]",
                border_style="red"
            ))
            console.print()

if __name__ == "__main__":
    main()
