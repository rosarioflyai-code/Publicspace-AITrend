from sqlalchemy.orm import Session
from . import models, schemas
import datetime

def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()

def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(
        title=article.title,
        article=article.article,
        image_url=article.image_url,
        date=datetime.datetime.now()
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article