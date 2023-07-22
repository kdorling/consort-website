from django import template

from menus.models import Menu

register = template.Library()


@register.simple_tag()
def to_id(str):
    return str.lower().replace(" ", "-")
