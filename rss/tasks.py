import os
import sys

import django
from django.db import transaction

import feedparser
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from rss.models import Feed, BaseLinks

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)


def get_new_feeds():
    try:
        for link in BaseLinks.objects.values_list('base_link', flat=True):
            logger.info(f"Parsing RSS link: {link}")
            parse(link)
    except Exception as e:
        logger.error(str(e))
        raise e


def parse(rss_link):
    feeds = feedparser.parse(rss_link)
    for feed in feeds['entries']:
        with transaction.atomic():
            Feed.objects.select_for_update().get_or_create(title=feed.title,
                                   link=feed.link,
                                   base_link=BaseLinks.objects.get(base_link=rss_link))


get_new_feeds()
