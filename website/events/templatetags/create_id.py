from django import template

register = template.Library()

@register.simple_tag
def create_id(value):
    """Removes all values of arg from the given string"""
    return value.replace(" ", "_").lower()