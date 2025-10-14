from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
import asyncio
from genkit.ai import Genkit
from genkit.plugins.google_genai import GoogleAI

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/articles/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = crud.get_articles(db, skip=skip, limit=limit)
    return articles

@app.post("/articles/", response_model=schemas.Article)
async def generate_article(db: Session = Depends(get_db)):
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

    # For now, we'll use a placeholder image
    image_url = "https://placehold.co/600x400"

    article = schemas.ArticleCreate(title=title, article=article_text, image_url=image_url)
    return crud.create_article(db=db, article=article)
