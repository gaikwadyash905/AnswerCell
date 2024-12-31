import os

def setup_openai_key(api_key):
    # Save the OpenAI API key to a file.
    key_file_path = os.path.expanduser("~/.openai_key.txt")
    try:
        with open(key_file_path, "w") as file:
            file.write(api_key)
        return "API Key Saved Successfully"
    except Exception as e:
        return f"Error saving API key: {e}"

def get_openai_key():
    # Retrieve the OpenAI API key from the file.
    key_file_path = os.path.expanduser("~/.openai_key.txt")
    try:
        with open(key_file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None
