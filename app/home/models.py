from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from django.shortcuts import redirect
from django.utils.html import format_html

from flex import blocks

from base.models import BasePage


class HomePage(BasePage):

    banner_title = models.CharField(
        max_length=50,
        help_text="The banner's title",
        blank=True,
        null=True,
    )

    banner_title_emphasis = models.CharField(
        max_length=50,
        help_text="The emphasized part of the banner's title",
        blank=True,
        null=True,
    )

    banner_text = RichTextField(
        help_text="Text under the banner",
        blank=True,
        null=True,
    )

    banner_buttons = StreamField([
            ("buttons", blocks.ButtonsBlock()),
        ],
        use_json_field=True,
        blank=True,
        null=True)

    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL,
    )

    include_banner = models.BooleanField(
        default=True,
        help_text="Include banner in the page"
    )

    body = StreamField([
            ("section", blocks.HomepageSection()),
        ], 
        use_json_field=True)

    content_panels = BasePage.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_title_emphasis"),
        FieldPanel("banner_text"),
        FieldPanel("banner_buttons"),
        FieldPanel("banner_background_image"),
        FieldPanel("include_banner"),
        FieldPanel("body"),
    ]
