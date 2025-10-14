from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(DateTime)
    article = Column(String)
    image_url = Column(String)