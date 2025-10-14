import os
from genkit.plugins.google_genai.google import GoogleAI

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set the GEMINI_API_KEY environment variable.")
    plugin = GoogleAI(api_key=api_key)
    for action in plugin.list_actions:
        print(action)

if __name__ == "__main__":
    main()
