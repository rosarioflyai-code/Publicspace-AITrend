from pydantic import BaseModel
import datetime

class ArticleBase(BaseModel):
    title: str
    article: str
    image_url: str

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int
    date: datetime.datetime

    class Config:
        orm_mode = True