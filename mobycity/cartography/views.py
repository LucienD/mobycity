from django.shortcuts import render
from django.core import serializers

from cartography.models import Category, PointOfInterest


def index(request):
    category_list = Category.objects.order_by('name')
    category_list_json = serializers.serialize('json', category_list)
    point_of_interest_list_json = serializers.serialize('json', PointOfInterest.objects.all())
    
    context = {
        'category_list' : category_list,
        'category_list_json' : category_list_json,
        'point_of_interest_list_json' : point_of_interest_list_json,
    }
    
    return render(request, 'cartography/index.html', context)