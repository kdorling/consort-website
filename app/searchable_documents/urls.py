from django.urls import path

from . import views


urlpatterns = [
    # /events/
    path("", views.index, name="index"),
]