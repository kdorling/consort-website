from django import template
from django.core.cache import cache

from weather.models import AirQuality
from weather.models import Forecast


register = template.Library()


@register.simple_tag
def any_weather():
    any_weather = cache.get("any_weather")
    if any_weather is None:
        any_weather = Forecast.objects.count() > 0
        cache.set("any_weather", any_weather, 3600)
    return any_weather


@register.simple_tag
def current_weather():
    current_weather = cache.get("current_weather")
    if current_weather is None:
        current_weather = Forecast.objects.filter(forecast_index=0).first()
        cache.set("current_weather", current_weather, 3600)
    return current_weather


@register.simple_tag
def forecast():
    forecast = cache.get("forecast")
    if forecast is None:
        forecast = Forecast.objects.filter(forecast_index__gte=1).all()
        cache.set("forecast", forecast, 3600)
    return forecast


@register.simple_tag
def any_airquality():
    any_airquality = cache.get("any_airquality")
    if any_airquality is None:
        any_airquality = AirQuality.objects.count() > 0
        cache.set("any_airquality", any_airquality, 3600)
    return any_airquality


@register.simple_tag
def get_airquality():
    airquality = cache.get("airquality")
    if airquality is None:
        airquality = AirQuality.objects.first()
        cache.set("airquality", airquality, 3600)
    return airquality


@register.simple_tag
def airquality_description(airquality):
    if airquality > 300:
        return "emergency"
    elif airquality > 200:
        return "very unhealthy"
    elif airquality > 150:
        return "unhealthy"
    elif airquality > 100:
        return "unhealthy for sensitive groups"
    elif airquality > 50:
        return "moderate"
    else:
        return "good"


@register.simple_tag
def airquality_color(airquality):
    if airquality > 300:
        return "text-purple-900"
    elif airquality > 200:
        return "text-red-900"
    elif airquality > 150:
        return "text-red-700"
    elif airquality > 100:
        return "text-orange-700"
    elif airquality > 50:
        return "text-yellow-500"
    else:
        return "text-green-500"
