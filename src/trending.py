
import asyncio
from genkit.ai import Genkit
from genkit.plugins.google_genai import GoogleAI

async def main():
    genkit = Genkit(
        plugins=[GoogleAI()],
        model='googleai/gemini-pro-latest',
    )

    prompt = "Write a short paragraph about the current state of Artificial Intelligence."

    response = await genkit.generate(prompt=prompt)

    print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
