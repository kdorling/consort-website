from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock

from base.models import BasePage

from information import blocks

class InformationPage(BasePage):
    body = StreamField([
        ("section", blocks.SectionBlock()),
        ("text", RichTextBlock()),
    ], null=True, blank=True, use_json_field=True)

    content_panels = BasePage.content_panels + [
        FieldPanel("body"),
    ]
