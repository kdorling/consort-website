from django import template
from weather.models import AirQuality
from weather.models import Forecast


register = template.Library()


@register.simple_tag
def any_weather():
    any_weather = Forecast.objects.count() > 0
    return any_weather


@register.simple_tag
def current_weather():
    current_weather = Forecast.objects.filter(forecast_index=0).first()
    return current_weather


@register.simple_tag
def forecast():
    forecast = Forecast.objects.filter(forecast_index__gte=1).all()
    return forecast


@register.simple_tag
def any_airquality():
    any_airquality = AirQuality.objects.count() > 0
    return any_airquality


@register.simple_tag
def get_airquality():
    airquality = AirQuality.objects.first()
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
