import datetime
from humanize import naturaltime

import pytz
from django import template

register = template.Library()


@register.filter
def get_time(upload_datetime):
    print(type(upload_datetime), upload_datetime)
    time_ago = datetime.datetime.now(tz=pytz.utc) - upload_datetime.replace(tzinfo=pytz.utc)
    if time_ago < datetime.timedelta(days=1):
        return naturaltime(time_ago)
    else:
        return upload_datetime.strftime("%Y-%m-%d %H:%M")


@register.filter
def check(arg):
    return 'check'
