import json

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Business, Category

def index(request):
    template = loader.get_template("business_directory/index.html")
    return HttpResponse(template.render(None, request))


def businesses(request):
    limit_parameter = request.GET.get('limit')

    if not limit_parameter:
        limit_parameter = 10

    if type(limit_parameter) is str and not limit_parameter.isnumeric():
        return JsonResponse({
        'status_code': 400,
        'error': 'Limit parameter should be an integer'
        })

    limit_parameter = int(limit_parameter)
    
    offset_parameter = request.GET.get('offset')

    if not offset_parameter:
        offset_parameter = 0

    if type(offset_parameter) is str and not offset_parameter.isnumeric():
        return JsonResponse({
        'status_code': 400,
        'error': 'Offset parameter should be an integer'
        })

    offset_parameter = int(offset_parameter)

    categories = request.GET.get('category')

    if categories and len(categories):
        business_list = Business.objects.filter(category__in=categories)
    else:
        business_list = Business.objects.all()

    paginator = Paginator(business_list, per_page=limit_parameter)
    businesses = list(paginator.get_page(offset_parameter))

    return JsonResponse({"businesses": [business.to_json() for business in businesses]})


def tags(request):
    tag_list = Category.objects.all()
    return JsonResponse({"tags": {category.tag.pk: category.tag.name for category in tag_list}})