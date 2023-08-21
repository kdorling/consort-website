import datetime
from django.db import models

from bs4 import BeautifulSoup

from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.search import index

from base.models import BasePage
from flex import blocks


class NewsPage(BasePage):
    subpage_types = ["news.PostPage"]


class PostPage(BasePage):
    date = models.DateField("date", blank=False, null=False, help_text="The date of the article.", default=datetime.date.today)

    summary = models.CharField(
        max_length=255,
        default="",
        blank=True,
        help_text="The summary displayed on the homepage and alert bar. Leave blank to automatically generate.",
    )

    class AlertLevel(models.IntegerChoices):
        NONE = 0
        GREEN = 1
        WARNING = 2
        DANGER = 3
                
    alert_level = models.IntegerField(
        choices=AlertLevel.choices,
        default=AlertLevel.NONE,
        help_text="The level of the alert banner at the top of the page.",
    )

    body = StreamField([
        ("section", blocks.SectionBlock()),
    ], null=True, blank=True, use_json_field=True)

    content_panels = BasePage.content_panels + [
        FieldPanel("date"),
        FieldPanel("summary"),
        FieldPanel("alert_level"),
        FieldPanel("body", classname="full"),
    ]

    search_fields = BasePage.search_fields + [
        index.SearchField("body"),
        index.AutocompleteField("body"),
    ]

    parent_page_types = ["news.NewsPage"]
    subpage_types = []
    

    def update_summary_if_empty(self):
        if (self.summary and self.summary != ""):
            return

        soup = BeautifulSoup(self.body.stream_block.render_basic(self.body), "html.parser")

        # Extract first paragraph from stream blocks
        text_data_array = []
        for tag in soup.find_all(['p']):
            text_data_array.append(tag.get_text())

        # Make the summary the first paragraph
        text_data = text_data_array[0]
        self.summary = text_data


    # def save_revision(self, **kwargs):
    #     self.update_description_if_empty()
    #     super().save_revision(**kwargs)


    def save(self, **kwargs):
        self.update_summary_if_empty()
        super().save(**kwargs)
    
    class Meta:
        verbose_name = "News Article Page"
        verbose_name_plural = "News Article Pages"