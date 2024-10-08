from celery import Celery
import json

# Create the Celery app
app = Celery('celery_tasks', broker='redis://localhost:6379/0')

# Optional configuration
app.conf.update(
    result_backend='redis://localhost:6379/0',
    task_serializer='json',
)

# Define your task
@app.task
def process_article(article_id):
    # Simulating article processing
    print(f"Processing article with ID {article_id}")

    # Create a dictionary with the processed article data
    article_data = {
        "article_id": article_id,
        "status": "processed"
    }

    # Save to JSON file
    save_to_json(article_data)

    return f"Processing article with ID {article_id}"

def save_to_json(article_data):
    try:
        with open('processed_articles.json', 'a') as json_file:
            json.dump(article_data, json_file)
            json_file.write('\n')
    except Exception as e:
        print(f"Error saving to JSON: {e}")
