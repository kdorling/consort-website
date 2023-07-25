from django.urls import path

from . import views

urlpatterns = [
    # /directory/
    path("", views.index, name="index"),
]