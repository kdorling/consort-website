import datetime
from django.db.models import Max, Min
from django.http import HttpResponse
from django.template import loader

from .models import SingleEvent
import json

def index(request):
    #annotate(num_books=Count("book"))
    #event_list = Event.objects.annotate(min_date=Min("times__date"), max_date=Max("times__date")).exclude(max_date__lt=datetime.date.today()).order_by("min_date")
    event_list = SingleEvent.objects.filter(live=True).filter(featured=True).filter(end_time__gte=datetime.date.today()).order_by("end_time")
    template = loader.get_template("events/index.html")
    context = {
        "event_list": event_list,
    }
    return HttpResponse(template.render(context, request))

def calendar(request):
    event_list = SingleEvent.objects.filter(live=True).filter(end_time__gte=datetime.date.today()-datetime.timedelta(days=30)).filter(end_time__lte=datetime.date.today()+datetime.timedelta(days=30))

    calendar_events = []

    for event in event_list:
        new_event = {
            "id": event.pk,
            "title": event.name,
            "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "description": event.description,
        }
        calendar_events.append(new_event)

    template = loader.get_template("events/calendar.html")
    context = {
        "event_list": json.dumps({
            "events": calendar_events,
            "initialView": "dayGridMonth"
        }),
    }
    return HttpResponse(template.render(context, request))