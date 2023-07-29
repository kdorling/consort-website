from django.urls import path

from . import views


urlpatterns = [
    # /miscellaneous/
    path("top_nav_bar", views.top_nav_bar, name="top_nav_bar"),
]