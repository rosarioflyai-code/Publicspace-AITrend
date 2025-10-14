import asyncio
import datetime
import json
from genkit.ai import Genkit
from genkit.plugins.google_genai import GoogleAI

async def main():
    # Initialize Genkit
    genkit = Genkit(
        plugins=[GoogleAI()],
    )

    # Generate the article
    prompt = "Write an article about the latest trends in AI."
    response = await genkit.generate(
        model="googleai/gemini-pro-latest",
        prompt=prompt
    )
    article_text = response.text

    # Generate the title
    prompt = f"Generate a short, catchy title for the following article:\n\n{article_text}"
    response = await genkit.generate(
        model="googleai/gemini-pro-latest",
        prompt=prompt
    )
    title = response.text.strip()

    image_url = "https://placehold.co/600x400"

    # Get the current date and time
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Create the data dictionary
    data = {
        "title": title,
        "date": date_str,
        "article": article_text,
        "image_url": image_url
    }

    # Save the data to a JSON file
    filepath = "/home/rosarioflyai/Publicspace-AITrend/site/data.json"
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Successfully generated content and saved it to {filepath}")

if __name__ == "__main__":
    asyncio.run(main())