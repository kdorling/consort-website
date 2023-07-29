from itertools import chain

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.models import Page
from wagtail.documents.models import Document
from wagtail.search.models import Query
from wagtail.search.query import Fuzzy


def get_search_quote(search_result):
    if "information" in search_result.page_type_display_name.lower():
        body_elements = search_result.specific


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        page_results = Page.objects.live().search(Fuzzy(search_query))
        document_results  = Document.objects.search(search_query)
        search_results = list(chain(page_results, document_results))

        if len(search_results) == 0:
            page_results = Page.objects.live().autocomplete(search_query)
            search_results = list(chain(page_results, document_results))

        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    for result in search_results:
        if result.highlights_:
            result.highlights_ = set(result.highlights_)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
