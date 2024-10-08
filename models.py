from sqlalchemy import Column, String, DateTime, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    content = Column(Text)
    pub_date = Column(DateTime)
    source_url = Column(String)
    category = Column(String)

# Database setup
DATABASE_URL = "postgresql://username:password@localhost/newsdb"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
