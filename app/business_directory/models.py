from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import LockableMixin, RevisionMixin, WorkflowMixin, DraftStateMixin, ClusterableModel
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class Category(TaggedItemBase):
    content_object = ParentalKey(
        "business_directory.Business",
        on_delete=models.CASCADE,
        related_name="tags",
    )

    def __str__(self):
        return self.name


@register_snippet
class Business(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, ClusterableModel):
    name = models.TextField(
        max_length=50,
        default="",
        help_text="The name of the business",
    )

    categories = ClusterTaggableManager(
        through=Category,
        blank=False,
        verbose_name="Categories",
        help_text="A comma-separated list of categories",
    )

    contact_name = models.TextField(
        max_length=50,
        blank=True,
        null=True,
        help_text="The name of the business's contact",
    )

    address = models.TextField(
        max_length=50,
        default="",
        help_text="The business's address"
    )

    website = models.TextField(
        max_length=50,
        blank=True,
        null=True,
        help_text="The business's website",
    )

    phone_number = models.TextField(
        max_length=50,
        blank=True,
        null=True,
        help_text="The business's phone number"
    )

    fax_number = models.TextField(
        max_length=50,
        blank=True,
        null=True,
        help_text="The business's fax number"
    )

    description = RichTextField(
        help_text="The description of the business",
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('categories'),
        FieldPanel('contact_name'),
        FieldPanel('address'),
        FieldPanel('website'),
        FieldPanel('phone_number'),
        FieldPanel('fax_number'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.name
