from django.http import Http404
from django.shortcuts import render


def top_nav_bar(request):
    return render(request, "components/top_nav_bar.html")
