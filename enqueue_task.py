from celery_tasks import process_article

# Enqueue tasks correctly
for i in range(1, 4):
    result = process_article.delay(i)
    print(f"Task for article {i} enqueued. Task ID: {result.id}")
