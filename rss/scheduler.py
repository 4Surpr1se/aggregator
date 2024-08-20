import logging
import os
import sys

import django

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from rss.tasks import get_new_feeds
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(get_new_feeds, 'interval', minutes=1)

if __name__ == '__main__':
    print("Starting scheduler...")
    try:
        scheduler.start()
    except Exception as e:
        logger.error("Error starting scheduler: %s", e)
