from django import template

from menus.models import Menu

register = template.Library()


@register.simple_tag()
def get_child_menu(page):
    menu_items = page.get_children().live().in_menu()
    print(menu_items[0])
    print(dir(menu_items[0]))
    return menu_items


@register.simple_tag()
def get_menu(slug):
    try:
        return Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return Menu.objects.none()


@register.simple_tag()
def is_empty(items):
    return not len(items.get_children().live().in_menu())
