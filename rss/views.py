from django.core.paginator import Paginator
from django.shortcuts import render

from rss.models import Feed


# Create your views here.

def index(request):
    posts = Feed.objects.all().order_by('-created_at')
    size = request.GET.get("size", 20)
    paginator = Paginator(posts, size)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'total': paginator.num_pages,
                                          'current_page': page_obj.number,
                                          'previous_page': page_obj.previous_page_number() if page_obj.has_previous() else '',
                                          'next_page': page_obj.next_page_number() if page_obj.has_next() else ''})
