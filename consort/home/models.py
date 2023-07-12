from django.db import models
from wagtail.admin.panels import FieldPanel, PageChooserPanel, MultiFieldPanel
from django.shortcuts import redirect
from django.utils.html import format_html

from base.models import BasePage


def create_small_information_link(description):
    item_text = models.CharField(
        max_length=25,
        default="",
        blank=False,
        help_text=f"Text for {description}",
    )

    item_icon = models.CharField(
        max_length=25,
        default="",
        blank=False,
        help_text=f"Icon for {description}",
    )

    item_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        related_name="+",
        help_text=f"Link for {description}",
        on_delete=models.SET_NULL,
    )

    return item_text, item_icon, item_link


def create_large_information_link(description):
    item_text = models.CharField(
        max_length=25,
        default="",
        blank=False,
        help_text=f"Text for {description}",
    )

    item_subtext = models.CharField(
        max_length=25,
        default="",
        blank=False,
        help_text=f"Subtext for {description}",
    )

    item_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text=f"Image for {description}",
        on_delete=models.SET_NULL,
    )

    item_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        related_name="+",
        help_text=f"Link for {description}",
        on_delete=models.SET_NULL,
    )

    return item_text, item_subtext, item_image, item_link

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
    # Banner section

    banner_title = models.CharField(
        max_length=50,
        blank=True,
        help_text="The banner title",
    )

    banner_subtitle = models.CharField(
        max_length=150,
        blank=True,
        help_text="Text under the banner title",
    )

    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL,
    )

    banner_button1_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        related_name="+",
        help_text="Link for first button on the banner",
        on_delete=models.SET_NULL,
    )

    banner_button1_text = models.CharField(
        max_length=50,
        default="Why Move",
        blank=False,
        help_text="Text for first button on the banner",
    )

    banner_button2_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        related_name="+",
        help_text="Link for second button on the banner",
        on_delete=models.SET_NULL,
    )

    banner_button2_text = models.CharField(
        max_length=50,
        default="Open a Business",
        blank=False,
        help_text="Text for second button on the banner",
    )

    banner_button3_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        related_name="+",
        help_text="Third button on the banner",
        on_delete=models.SET_NULL,
    )

    banner_button3_text = models.CharField(
        max_length=50,
        default="Job Board",
        blank=False,
        help_text="Text for third button on the banner",
    )

    # Information section

    information_title = models.CharField(
        max_length=50,
        default="Information",
        blank=False,
        help_text="Information section title text",
    )

    # Residents section

    residents_button_text = models.CharField(
        max_length=25,
        default="Residents",
        blank=False,
        help_text="Text for the residents button",
    )

    residents_small_item1_text, residents_small_item1_icon, residents_small_item1_link = \
        create_small_information_link("first small residents item")

    residents_small_item2_text, residents_small_item2_icon, residents_small_item2_link = \
        create_small_information_link("second small residents item")

    residents_small_item3_text, residents_small_item3_icon, residents_small_item3_link = \
        create_small_information_link("third small residents item")

    residents_small_item4_text, residents_small_item4_icon, residents_small_item4_link = \
        create_small_information_link("fourth small residents item")

    residents_large_item1_text, residents_large_item1_subtext, \
        residents_large_item1_image, residents_large_item1_link = \
        create_large_information_link("first large residents item")

    residents_large_item2_text, residents_large_item2_subtext, \
        residents_large_item2_image, residents_large_item2_link = \
        create_large_information_link("second large residents item")

    businesses_button_text = models.CharField(
        max_length=25,
        default="Businesses",
        blank=False,
        help_text="Text for the businesses button",
    )

    businesses_small_item1_text, businesses_small_item1_icon, businesses_small_item1_link = \
        create_small_information_link("first small businesses item")

    businesses_small_item2_text, businesses_small_item2_icon, businesses_small_item2_link = \
        create_small_information_link("second small businesses item")

    businesses_small_item3_text, businesses_small_item3_icon, businesses_small_item3_link = \
        create_small_information_link("third small businesses item")

    businesses_small_item4_text, businesses_small_item4_icon, businesses_small_item4_link = \
        create_small_information_link("fourth small businesses item")

    businesses_large_item1_text, businesses_large_item1_subtext, \
        businesses_large_item1_image, businesses_large_item1_link = \
        create_large_information_link("first large businesses item")

    businesses_large_item2_text, businesses_large_item2_subtext, \
        businesses_large_item2_image, businesses_large_item2_link = \
        create_large_information_link("second large businesses item")

    visitors_button_text = models.CharField(
        max_length=25,
        default="Visitors",
        blank=False,
        help_text="Text for the visitors button",
    )

    visitors_small_item1_text, visitors_small_item1_icon, visitors_small_item1_link = \
        create_small_information_link("first small visitors item")

    visitors_small_item2_text, visitors_small_item2_icon, visitors_small_item2_link = \
        create_small_information_link("second small visitors item")

    visitors_small_item3_text, visitors_small_item3_icon, visitors_small_item3_link = \
        create_small_information_link("third small visitors item")

    visitors_small_item4_text, visitors_small_item4_icon, visitors_small_item4_link = \
        create_small_information_link("fourth small visitors item")

    visitors_large_item1_text, visitors_large_item1_subtext, \
        visitors_large_item1_image, visitors_large_item1_link = \
        create_large_information_link("first large visitors item")

    visitors_large_item2_text, visitors_large_item2_subtext, \
        visitors_large_item2_image, visitors_large_item2_link = \
        create_large_information_link("second large visitors item")

    # Popular pages section

    popular_pages_title = models.CharField(
        max_length=50,
        default="Popular Pages",
        blank=False,
        help_text="Popular pages section title text",
    )

    popular_pages_item1_text, popular_pages_item1_icon, popular_pages_item1_link = \
        create_small_information_link("first popular page")

    popular_pages_item2_text, popular_pages_item2_icon, popular_pages_item2_link = \
        create_small_information_link("second popular page")

    popular_pages_item3_text, popular_pages_item3_icon, popular_pages_item3_link = \
        create_small_information_link("third popular page")

    popular_pages_item4_text, popular_pages_item4_icon, popular_pages_item4_link = \
        create_small_information_link("fourth popular page")

    content_panels = BasePage.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            FieldPanel("banner_background_image"),
            FieldPanel("banner_button1_text"),
            PageChooserPanel("banner_button1_link"),
            FieldPanel("banner_button2_text"),
            PageChooserPanel("banner_button2_link"),
            FieldPanel("banner_button3_text"),
            PageChooserPanel("banner_button3_link"),
        ], heading="Banner"),
        # MultiFieldPanel([
        #     FieldPanel("information_title"),
        #     ], heading="Information"),
        # MultiFieldPanel([
        #     FieldPanel("residents_button_text"),
        #     FieldPanel("residents_small_item1_text"),
        #     FieldPanel("residents_small_item1_icon"),
        #     PageChooserPanel("residents_small_item1_link"),
        #     FieldPanel("residents_small_item2_text"),
        #     FieldPanel("residents_small_item2_icon"),
        #     PageChooserPanel("residents_small_item2_link"),
        #     FieldPanel("residents_small_item3_text"),
        #     FieldPanel("residents_small_item3_icon"),
        #     PageChooserPanel("residents_small_item3_link"),
        #     FieldPanel("residents_small_item4_text"),
        #     FieldPanel("residents_small_item4_icon"),
        #     PageChooserPanel("residents_small_item4_link"),
        #     FieldPanel("residents_large_item1_text"),
        #     FieldPanel("residents_large_item1_subtext"),
        #     FieldPanel("residents_large_item1_image"),
        #     PageChooserPanel("residents_large_item1_link"),
        #     FieldPanel("residents_large_item2_text"),
        #     FieldPanel("residents_large_item2_subtext"),
        #     FieldPanel("residents_large_item2_image"),
        #     PageChooserPanel("residents_large_item2_link"),
        # ], heading="Residents"),
        # MultiFieldPanel([
        #     FieldPanel("businesses_button_text"),
        #     FieldPanel("businesses_small_item1_text"),
        #     FieldPanel("businesses_small_item1_icon"),
        #     PageChooserPanel("businesses_small_item1_link"),
        #     FieldPanel("businesses_small_item2_text"),
        #     FieldPanel("businesses_small_item2_icon"),
        #     PageChooserPanel("businesses_small_item2_link"),
        #     FieldPanel("businesses_small_item3_text"),
        #     FieldPanel("businesses_small_item3_icon"),
        #     PageChooserPanel("businesses_small_item3_link"),
        #     FieldPanel("businesses_small_item4_text"),
        #     FieldPanel("businesses_small_item4_icon"),
        #     PageChooserPanel("businesses_small_item4_link"),
        #     FieldPanel("businesses_large_item1_text"),
        #     FieldPanel("businesses_large_item1_subtext"),
        #     FieldPanel("businesses_large_item1_image"),
        #     PageChooserPanel("businesses_large_item1_link"),
        #     FieldPanel("businesses_large_item2_text"),
        #     FieldPanel("businesses_large_item2_subtext"),
        #     FieldPanel("businesses_large_item2_image"),
        #     PageChooserPanel("businesses_large_item2_link"),
        # ], heading="Businesses"),
        # MultiFieldPanel([
        #     FieldPanel("visitors_button_text"),
        #     FieldPanel("visitors_small_item1_text"),
        #     FieldPanel("visitors_small_item1_icon"),
        #     PageChooserPanel("visitors_small_item1_link"),
        #     FieldPanel("visitors_small_item2_text"),
        #     FieldPanel("visitors_small_item2_icon"),
        #     PageChooserPanel("visitors_small_item2_link"),
        #     FieldPanel("visitors_small_item3_text"),
        #     FieldPanel("visitors_small_item3_icon"),
        #     PageChooserPanel("visitors_small_item3_link"),
        #     FieldPanel("visitors_small_item4_text"),
        #     FieldPanel("visitors_small_item4_icon"),
        #     PageChooserPanel("visitors_small_item4_link"),
        #     FieldPanel("visitors_large_item1_text"),
        #     FieldPanel("visitors_large_item1_subtext"),
        #     FieldPanel("visitors_large_item1_image"),
        #     PageChooserPanel("visitors_large_item1_link"),
        #     FieldPanel("visitors_large_item2_text"),
        #     FieldPanel("visitors_large_item2_subtext"),
        #     FieldPanel("visitors_large_item2_image"),
        #     PageChooserPanel("visitors_large_item2_link"),
        # ], heading="Visitors"),
        # MultiFieldPanel([
        #     FieldPanel("popular_pages_title"),
        #     FieldPanel("popular_pages_item1_text"),
        #     FieldPanel("popular_pages_item1_icon"),
        #     PageChooserPanel("popular_pages_item1_link"),
        #     FieldPanel("popular_pages_item2_text"),
        #     FieldPanel("popular_pages_item2_icon"),
        #     PageChooserPanel("popular_pages_item2_link"),
        #     FieldPanel("popular_pages_item3_text"),
        #     FieldPanel("popular_pages_item3_icon"),
        #     PageChooserPanel("popular_pages_item3_link"),
        #     FieldPanel("popular_pages_item4_text"),
        #     FieldPanel("popular_pages_item4_icon"),
        #     PageChooserPanel("popular_pages_item4_link"),
        # ], heading="Popular Pages"),
    ]
