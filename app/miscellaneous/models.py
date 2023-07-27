from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from django.shortcuts import redirect
from django.utils.html import format_html

from flex import blocks

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

    def get_url(self, request=None, current_site=None):
        return self.redirect_to

    def get_full_url(self, request=None, current_site=None):
        return self.redirect_to

    def serve(self, request):
        return redirect(self.redirect_to)

    def serve_preview(self, request, preview_mode):
        return redirect(self.redirect_to)


class IndexPage(BasePage):
    pass