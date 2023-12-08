from django.db import models
from django.utils.decorators import method_decorator

from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.search import index

from wagtailcache.cache import cache_page, WagtailCacheMixin


from base.models import BasePage
from . import blocks

@method_decorator(cache_page, name='serve')
class FlexPage(WagtailCacheMixin, BasePage):
    body = StreamField([
        ("section", blocks.SectionBlock()),
    ], null=True, blank=True, use_json_field=True)

    include_scrollspy = models.BooleanField(
        default=False,
        help_text="Include scrollspy in the page"
    )

    content_panels = BasePage.content_panels + [
        # FieldPanel("include_scrollspy"),
        FieldPanel("body"),
    ]

    search_fields = BasePage.search_fields + [
        index.SearchField("body"),
        index.AutocompleteField("body"),
    ]

    class Meta:
        verbose_name = " Information / Flex Page"
        verbose_name_plural = "Informatoin / Flex Page"