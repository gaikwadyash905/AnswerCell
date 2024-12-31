from xlwings_handler import setup_openai_key

if __name__ == "__main__":
    print("OpenAI Excel Integration Setup")
    api_key = input("Enter your OpenAI API key: ")
    message = setup_openai_key(api_key)
    print(message)
