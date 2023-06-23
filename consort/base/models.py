from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class BasePage(Page):
    icon = models.CharField(
        max_length=25,
        default="",
        blank=False,
        help_text=f"The page's icon",
    )

    description = models.CharField(
        max_length=50,
        default="",
        blank=False,
        help_text=f"The page's description. Used in the menu and on cards",
    )

    content_panels = Page.content_panels + [
        FieldPanel("icon"),
        FieldPanel("description"),
    ]