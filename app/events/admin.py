from tokenize import Single
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import Event


@modeladmin_register
class EventAdmin(ModelAdmin):
    """Event admin."""

    model = Event
    menu_label = "Events"
    menu_icon = "date"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "description", "start_time", "end_time")
    search_fields = ("name", "description")
