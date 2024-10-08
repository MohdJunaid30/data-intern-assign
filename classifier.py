import spacy
from models import Article, session

nlp = spacy.load('en_core_web_sm')

categories = {
    "terrorism": "Terrorism / protest / political unrest / riot",
    "positive": "Positive/Uplifting",
    "disaster": "Natural Disasters",
    "others": "Others"
}

def classify_article(article_id):
    article = session.query(Article).filter_by(id=article_id).first()
    if not article:
        return

    doc = nlp(article.content.lower())
    
    if "protest" in article.content or "riot" in article.content or "terrorism" in article.content:
        article.category = categories["terrorism"]
    elif "positive" in article.content or "uplifting" in article.content:
        article.category = categories["positive"]
    elif "earthquake" in article.content or "flood" in article.content or "disaster" in article.content:
        article.category = categories["disaster"]
    else:
        article.category = categories["others"]

    session.commit()
