from itertools import chain

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from pkg_resources import resource_isdir

from wagtail.models import Page
from wagtail.documents.models import Document
from wagtail.search.models import Query
from wagtail.search.query import Fuzzy, Phrase
from miscellaneous.models import IndexPage

from business_directory.models import Business
from custom_search.backends import get_search_backend


def get_search_quote(search_result):
    if "information" in search_result.page_type_display_name.lower():
        body_elements = search_result.specific

def unique_chain(*args, **kwargs):
    seen = set()
    for element in chain(*args, **kwargs):
        if element not in seen:
            seen.add(element)
            yield element

def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)
    show_scores = request.GET.get("show_scores", None)

    # Search
    if search_query:

        s = get_search_backend()

        if '"' in search_query:
            page_results = Page.objects.live().not_type(IndexPage).search(Phrase(search_query)).annotate_score("score_")
            business_results = s.search(Phrase(search_query), Business.objects.filter(live=True)).annotate_score("score_")
            document_results  = Document.objects.search(Phrase(search_query)).annotate_score("score_")
        else:
            page_results = Page.objects.live().not_type(IndexPage).search(search_query).annotate_score("score_")
            business_results = s.search(search_query, Business.objects.filter(live=True)).annotate_score("score_")
            document_results  = Document.objects.search(search_query).annotate_score("score_")

        if '"' not in search_query:
            fuzzy_page_results = Page.objects.live().not_type(IndexPage).search(Fuzzy(search_query)).annotate_score("score_")
            for result in fuzzy_page_results:
                result.score_ /= 5
            page_results = list(unique_chain(page_results, fuzzy_page_results))

            fuzzy_business_results = s.search(Fuzzy(search_query), Business.objects.filter(live=True)).annotate_score("score_")
            for result in fuzzy_business_results:
                result.score_ /= 5
            business_results = list(unique_chain(business_results, fuzzy_business_results))

            fuzzy_document_results = Document.objects.search(Fuzzy(search_query)).annotate_score("score_")
            for result in fuzzy_document_results:
                result.score_ /= 5
            document_results = list(unique_chain(document_results, fuzzy_document_results))

        if len(page_results) == 0 and '"' not in search_query:
            page_results = Page.objects.live().autocomplete(search_query).annotate_score("score_")
            for result in page_results:
                result.score_ /= 10

        if len(business_results) == 0 and '"' not in search_query:
            business_results = s.autocomplete(search_query, Business.objects.filter(live=True)).annotate_score("score_")
            for result in business_results:
                result.score_ /= 10

        if len(document_results) == 0 and '"' not in search_query:
            document_results = Document.objects.autocomplete(search_query).annotate_score("score_")
            for result in document_results:
                result.score_ /= 10
    
        search_results = list(chain(page_results, document_results, business_results))
        search_results = sorted(search_results, key=lambda result: result.score_, reverse=True)

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

    # result_map = {str(result): result for result in search_results}
    # search_results = list(result_map.values())

    for result in search_results:
        highlights = set()
        for highlight in result.highlights_:
            samples = highlight.split(" ")
            if len(samples) >= 5:
                highlights.add(highlight)
        if len(highlights) > 0:
            result.highlights_ = highlights

    # for result in search_results:
    #     highlights = set()
    #     if result.highlights_ and len(search_query) >= 3:        
    #         for highlight in result.highlights_:
    #             for sample in highlight.split("<em>"):
    #                 if len(sample) >= 3 and sample[:3].lower() == ''.join(filter(str.isalnum, search_query))[:3].lower():
    #                         highlights.add(highlight)
    #         result.highlights_ = highlights

    # search_results = [result for result in search_results if result.highlights_ or "page" in str(type(result)).lower()]
        
    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
            "show_scores": show_scores,
        },
    )
