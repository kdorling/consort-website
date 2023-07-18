from django.db import models

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, ClusterableModel, DraftStateMixin, LockableMixin, RevisionMixin, WorkflowMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class Profile(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
    name = models.CharField(
        max_length=50,
        help_text="The name of the council member"
    )

    photo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="The council member's photo",
        on_delete=models.SET_NULL,
    )

    email = models.CharField(
        max_length=50,
        help_text="The email address of the council member"
    )

    position = models.CharField(
        max_length=50,
        help_text="The council member's position"
    )

    panels = [
        FieldPanel("name"),        
        FieldPanel("photo"),
        FieldPanel("email"),
        FieldPanel("position"),
    ]

    def __str__(self):
        return self.name
