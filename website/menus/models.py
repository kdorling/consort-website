from django.db import models

from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.models import Orderable


class SubMenuItem(Orderable):
    page = models.ForeignKey(
        "base.BasePage",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )

    open_in_new_tab = models.BooleanField(default=False, blank=True)

    menu_item = ParentalKey("MenuItem", related_name="submenu_items")

    panels = [
        PageChooserPanel("page"),
        FieldPanel("open_in_new_tab"),
    ]


class MenuItem(Orderable, ClusterableModel):

    class Alignment(models.IntegerChoices):
        LEFT = 0, "Left"
        CENTER = 1, "Center"
        RIGHT = 2, "Right"

    page = models.ForeignKey(
        "base.BasePage",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )

    alignment = models.IntegerField(choices=Alignment.choices, blank=True, default=0)

    open_in_new_tab = models.BooleanField(default=False, blank=True)

    menu = ParentalKey("Menu", related_name="menu_items")

    panels = [
        PageChooserPanel("page"),
        FieldPanel("open_in_new_tab"),
        FieldPanel("alignment"),
        InlinePanel("submenu_items", heading="Submenu Items"),
    ]


class Menu(ClusterableModel):

    title = models.CharField(max_length=100)

    slug = AutoSlugField(
        populate_from="title",
        editable=True,
    )

    panels = [
        FieldPanel("title"),
        #PageChooserPanel("page"),
        FieldPanel("slug"),
        InlinePanel("menu_items", heading="Menu Items"),
    ]

    def __str__(self):
        return self.title
