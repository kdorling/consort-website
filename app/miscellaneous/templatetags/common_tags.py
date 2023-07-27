from django import template

from menus.models import Menu

register = template.Library()


@register.simple_tag()
def to_id(str):
    return str.lower().replace(" ", "-")


@register.simple_tag()
def is_section_type(item):
    return "section" in item.block_type.lower()


@register.simple_tag()
def is_title_type(item):
    return "title" in item.block_type.lower()


@register.simple_tag()
def item_type(item):
    return item.block_type