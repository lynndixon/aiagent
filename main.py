import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
content = sys.argv[1]

def main():
    if len(sys.argv) <= 1:
        print("Please provide input text as a command-line argument.")
        sys.exit(1)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[content],
    )
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    return print(f"{response.text} \nPrompt tokens: {prompt_tokens}, \nResponse tokens: {response_tokens}")


if __name__ == "__main__":
    main()
