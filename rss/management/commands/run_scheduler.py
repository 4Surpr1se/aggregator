from django.core.management.base import BaseCommand

from rss.scheduler import scheduler


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler.start()
