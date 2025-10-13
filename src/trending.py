
import asyncio
from genkit.ai import Genkit

async def main():
    genkit = Genkit()

    prompt = "Write a short paragraph about the current state of Artificial Intelligence."

    response = await genkit.generate(prompt=prompt)

    print(response.output)

if __name__ == "__main__":
    asyncio.run(main())
