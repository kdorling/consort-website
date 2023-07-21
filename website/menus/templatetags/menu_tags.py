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
    return not len(items)


@register.simple_tag()
def has_children(items):
    return not is_empty(items)


@register.simple_tag()
def is_none_or_empty(s):
    return s is None or len(s) == 0

@register.simple_tag()
def alignment_classes(alignment_value):
    match alignment_value:
        case 1:
            return "left-1/2 right-0 translate-x-[-50%]"
        case 2:
            return "right-0"
        case _:
            return ""
