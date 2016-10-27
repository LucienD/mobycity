from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from news.models import News


def list(request):
    news_list = News.objects.filter(publication_datetime__lt=timezone.now).order_by('-publication_datetime')
    paginator = Paginator(news_list, 5)
    
    page = request.GET.get('page')
    
    try:
        news_paginated_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_paginated_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_paginated_list = paginator.page(paginator.num_pages)
    
    context = {
        'news_list': news_paginated_list,
    }
    
    return render(request, 'news/list.html', context)