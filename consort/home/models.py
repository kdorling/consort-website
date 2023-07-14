from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from django.shortcuts import redirect
from django.utils.html import format_html

from common import blocks

from base.models import BasePage


# From: https://www.yellowduck.be/posts/creating-redirector-page-wagtail
class RedirectorPage(BasePage):
    redirect_to = models.URLField(
        help_text='The URL to redirect to',
        blank=False,
    )

    content_panels = BasePage.content_panels + [
        FieldPanel('redirect_to', classname="full"),
    ]

    def get_admin_display_title(self):
        return format_html(f"{self.draft_title}➡️ {self.redirect_to}")

    class Meta:
        verbose_name = 'Redirector'

    def get_url(self, request=None, current_site=None):
        return self.redirect_to

    def get_full_url(self, request=None, current_site=None):
        return self.redirect_to

    def serve(self, request):
        return redirect(self.redirect_to)

    def serve_preview(self, request, preview_mode):
        return redirect(self.redirect_to)


class HomePage(BasePage):

    banner_title = models.CharField(
        max_length=50,
        help_text="The banner's title"
    )

    banner_title_emphasis = models.CharField(
        max_length=50,
        help_text="The emphasized part of the banner's title"
    )

    banner_text = RichTextField(
        help_text="Text under the banner"
    )

    banner_buttons = StreamField([
        ("buttons", blocks.ButtonsBlock()),
    ], use_json_field=True)

    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL,
    )

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("tabs", blocks.PagesTabsBlock()),
    ], use_json_field=True)

    content_panels = BasePage.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_title_emphasis"),
        FieldPanel("banner_text"),
        FieldPanel("banner_buttons"),
        FieldPanel("banner_background_image"),
        FieldPanel("body"),
    ]