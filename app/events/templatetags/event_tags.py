import datetime

from django import template
from events.models import Event

register = template.Library()


@register.inclusion_tag("events/tags/event_list.html", takes_context=True)
def event_list(context):
    """Event list template tag."""
    request = context["request"]
    event_list = Event.objects.filter(live=True).filter(featured=True).filter(end_time__gte=datetime.date.today()).order_by("end_time")
    return {
        "request": request,
        "event_list": event_list,
    }
