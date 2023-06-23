from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock

from information import blocks

class InformationPage(Page):
    body = StreamField([
        ("section", blocks.SectionBlock()),
        ("text", RichTextBlock()),
    ], null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
