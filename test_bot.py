import os
import subprocess
import sys

# Force standard streams to use UTF-8 to prevent encoding issues
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


def run_tests():
    inputs = [
        "y",
        "What is a string in Python?",
        "exit",
    ]

    input_text = "\n".join(inputs) + "\n"
    print("Starting chatbot automated verification...")
    print("Running app.py and feeding inputs...")

    process = subprocess.Popen(
        [os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe"), "app.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        cwd=os.getcwd(),
    )

    try:
        stdout, stderr = process.communicate(input=input_text, timeout=20)
    except subprocess.TimeoutExpired:
        process.kill()
        raise AssertionError("Verification error: Subprocess timed out.")

    print("\n=== Chatbot Output Capture ===")
    print(stdout)
    print("==============================\n")

    if stderr:
        print("=== Error Log ===")
        print(stderr)
        print("=================\n")

    assert process.returncode == 0, f"Unexpected exit code: {process.returncode}"
    assert "string" in stdout.lower(), stdout
    assert "text" in stdout.lower() or "sequence" in stdout.lower(), stdout
    print("Automated verification passed.")


if __name__ == "__main__":
    run_tests()
