from django import template

from news.models import PostPage

register = template.Library()

@register.simple_tag()
def get_alerts():
    return PostPage.objects.filter(live=True).filter(alert_level__gt=0).order_by('-alert_level')

@register.simple_tag()
def get_preview_alerts():
    return PostPage.objects.filter(alert_level__gt=0).order_by('-alert_level')

@register.simple_tag()
def get_news():
    return PostPage.objects.filter(live=True).order_by('-date')[:3]

@register.simple_tag()
def get_preview_news():
    return PostPage.objects.order_by('-date')[:3]

@register.simple_tag()
def get_news_archive():
    return PostPage.objects.filter(live=True).order_by('-date')

@register.simple_tag()
def get_preview_news_archive():
    return PostPage.objects.order_by('-date')