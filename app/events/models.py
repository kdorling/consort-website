from django.core.exceptions import ValidationError
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.fields import RichTextField
from wagtail.models import Orderable, ClusterableModel, DraftStateMixin, LockableMixin, RevisionMixin, WorkflowMixin
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Event(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, models.Model):
       
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
        blank=True,
        null=True,
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
        help_text="Is this event featured? (Note: Recurring events cannot be featured.)",
        default=False,
    )

    rrule = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="Apply an RRULE to this event. (Note: Recurring events cannot be featured.)",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
        FieldPanel("description"),
        FieldPanel("start_time"),
        FieldPanel("end_time"),
        FieldPanel("featured"),
        FieldPanel("rrule"),
    ]

    def clean(self):
        if self.rrule != None:
            if self.rrule != "":
                if self.featured:
                    raise ValidationError("Recurring events cannot be featured.")
                
        if self.start_time != None and self.end_time != None:
            if self.start_time > self.end_time:
                raise ValidationError("The end time must be after the start time.")

    def __str__(self):
        return f"{self.name} from {self.start_time} to {self.end_time}"
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
