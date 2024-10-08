import feedparser
from models import Article, session
from celery_tasks import process_article
from datetime import datetime

feeds = [
    'http://rss.cnn.com/rss/cnn_topstories.rss',
    'http://qz.com/feed',
    'http://feeds.foxnews.com/foxnews/politics',
    'http://feeds.reuters.com/reuters/businessNews',
    'http://feeds.feedburner.com/NewshourWorld',
    'https://feeds.bbci.co.uk/news/world/asia/india/rss.xml'
]

def fetch_and_store_articles():
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            # Check for duplicates
            if session.query(Article).filter_by(title=entry.title).first():
                continue

            # Create new article instance
            article = Article(
                title=entry.title,
                content=entry.summary,
                pub_date=datetime(*entry.published_parsed[:6]),
                source_url=entry.link
            )

            session.add(article)
            session.commit()

            # Send the article to Celery for processing (categorization)
            process_article.delay(article.id)
