from django.urls import path

from . import views


urlpatterns = [
    # /directory/
    path("", views.index, name="index"),
    path("businesses/", views.businesses, name="businesses"),
    path("tags/", views.tags, name="tags"),
]