from django import template

register = template.Library()

@register.simple_tag
def format_date(value, format):
    """Removes all values of arg from the given string"""
    return value.strftime(format)

@register.simple_tag
def dates_equal(date1, date2):
    """Removes all values of arg from the given string"""
    return date1.date() == date2.date()