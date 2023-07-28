from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.search import index

from base.models import BasePage
from . import blocks

class FlexPage(BasePage):
    body = StreamField([
        ("section", blocks.SectionBlock()),
    ], null=True, blank=True, use_json_field=True)

    include_scrollspy = models.BooleanField(
        default=False,
        help_text="Include scrollspy in the page"
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("include_scrollspy"),
        FieldPanel("body"),
    ]

    search_fields = BasePage.search_fields + [
        index.SearchField("body"),
    ]

    class Meta:
        verbose_name = " Information / Flex Page"
        verbose_name_plural = "Informatoin / Flex Page"