from feed_parser import fetch_and_store_articles
from celery_tasks import app as celery_app

if __name__ == "__main__":
    fetch_and_store_articles()
