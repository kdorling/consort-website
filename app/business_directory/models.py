from django.db import models
from django.contrib.postgres.fields import ArrayField

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import LockableMixin, RevisionMixin, WorkflowMixin, DraftStateMixin, ClusterableModel
from wagtail.search import index
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
class Business(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, index.Indexed, ClusterableModel):
    name = models.TextField(
        max_length=50,
        default="",
        help_text="The name of the business",
    )

    categories = ClusterTaggableManager(
        through=Category,
        blank=False,
        verbose_name="Categories",
        help_text="A comma-separated list of categories. Businesses will be listed under these keywords on the directory page.",
    )

    search_keywords = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        default=list,
        help_text="A list of keywords for the business. These terms will be used when performing searches.",
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
        help_text="The business's address",
        blank=True,
        null=True,
    )

    google_maps_link = models.TextField(
        max_length=50,
        default="",
        help_text="A link to the business on Google Maps",
        blank=True,
        null=True,
    )

    mailing_address = models.TextField(
        max_length=50,
        default="",
        help_text="The business's mailing address",
        blank=True,
        null=True,
    )

    email_address = models.TextField(
        max_length=50,
        default="",
        help_text="The business's email address",
        blank=True,
        null=True,
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
        FieldPanel('search_keywords'),
        FieldPanel('contact_name'),
        FieldPanel('address'),
        FieldPanel('google_maps_link'),
        FieldPanel('mailing_address'),
        FieldPanel('email_address'),
        FieldPanel('website'),
        FieldPanel('phone_number'),
        FieldPanel('fax_number'),
        FieldPanel('description'),
    ]

    search_fields = [
        index.SearchField('name', boost=10),
        index.SearchField('search_keywords', boost=10),
        index.SearchField('description'),

        index.AutocompleteField('name', boost=10),
        index.AutocompleteField('search_keywords', boost=10),
        index.AutocompleteField('description'),

        index.FilterField('live')
    ]

    def __str__(self):
        return self.name
