from django.db import models


from modelcluster.fields import ParentalKey

from wagtail.fields import RichTextField
from wagtail.models import Orderable, ClusterableModel, DraftStateMixin, LockableMixin, RevisionMixin, WorkflowMixin
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet

#from events import blocks


#@register_snippet
class EventBase(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
    name = models.CharField(
        max_length=255,
        help_text="The name of the event"
    )
   
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        help_text="The image associated with the event",
        on_delete=models.SET_NULL,
    )

    description = RichTextField(
        help_text="The description of the event"
    )

    document = models.ForeignKey(
        "wagtaildocs.Document",
        blank=True,
        null=True,
        related_name="+",
        help_text="A document associated with the event",
        on_delete=models.SET_NULL,
    )

    all_day = models.BooleanField(
        help_text="Does this event last all day?",
        default=False,
    )

    panels = [
        FieldPanel("name"),        
        FieldPanel("image"),
        FieldPanel("description"),
        FieldPanel("document"),
        FieldPanel("all_day")
    ]

    def __str__(self):
        return self.name


@register_snippet
class SingleEvent(EventBase):
    start_time = models.DateTimeField(
        blank=False,
        null=True,
        help_text="The date and time when the event begins"
    )

    end_time = models.DateTimeField(
        blank=False,
        null=True,
        help_text="The date and time when the event ends"
    )

    featured = models.BooleanField(
        help_text="List this event on the featured events page?",
        default=False,    
    )

    panels = EventBase.panels + [
        FieldPanel("start_time"),
        FieldPanel("end_time"),
        FieldPanel("featured")
    ]

    def __str__(self):
        return self.name

