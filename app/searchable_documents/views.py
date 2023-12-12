from django.http import HttpResponse
from django.shortcuts import render

from searchable_documents.models import Document
from wagtail.models import Collection

def index(request):
    collection_name = request.GET.get("collection", None)
    order_by = request.GET.get("orderby", None)
    
    if collection_name == None or collection_name == "":
        response = HttpResponse(status=400)
        response.reason_phrase = "Key 'collection' is required"
        return response

    if order_by == None or order_by == "" or order_by not in ["title", "date", "-date", "-title"]:
        order_by = "title"

    collection = Collection.objects.filter(name=collection_name)
    if len(collection) == 0:
        response = HttpResponse(status=404)
        response.reason_phrase = "Collection {{collection}} not found"
        return response
    
    if "-" in order_by:
        sorted_minutes_children = sorted(collection[0].get_children(), reverse=True, key=lambda child: child.name);
    else:
        sorted_minutes_children = sorted(collection[0].get_children(), key=lambda child: child.name);

    collection_contents = {}
    for child in sorted_minutes_children:
        collection_contents[child.name] = {}
        documents_in_collection = Document.objects.filter(collection__name=child.name).order_by(order_by)
        for document in documents_in_collection:
            collection_contents[child.name][document.title] = document.url

    #import pdb; pdb.set_trace()

    return render(request, 'index.html', {"collection_name": collection_name, "collection_contents": collection_contents})