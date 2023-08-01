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

    FREQUENCY_CHOICES = [
        ("DAILY", "Daily"),
        ("WEEKLY", "Weekly"),
        ("MONTHLY", "Monthly"),
        ("YEARLY", "Yearly"),
    ]

    frequency = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        default="WEEKLY",
        choices=FREQUENCY_CHOICES,
        help_text="When does this event repeat?",
    )
    
    interval = models.IntegerField(
        blank=True,
        null=True,
        default=1,
        help_text="How often does this event occur?"
    )

    bymonth= models.IntegerField(
        blank=True,
        null=True,
        help_text="The month when this event occurs"
    )

    bymonthday = models.IntegerField(
        blank=True,
        null=True,
        help_text="The day of the month when this event occurs"
    )

    byyearday = models.IntegerField(
        blank=True,
        null=True,
        help_text="The day of the year when this event occurs"
    )

    byeaster = models.IntegerField(
        blank=True,
        null=True,
        help_text="The day of Easter"
    )

    byweekno = models.IntegerField(
        blank=True,
        null=True,
        help_text="The week of the year when this event occurs"
    )

    byweekday = models.IntegerField(
        blank=True,
        null=True,
        help_text="The day of the week when this event occurs"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
        FieldPanel("description"),
        FieldPanel("document"),
        FieldPanel("start_time"),
        FieldPanel("end_time"),
        FieldPanel("featured"),
        FieldPanel("frequency"),
        FieldPanel("interval"),
        FieldPanel("bymonth"),
        FieldPanel("bymonthday"),
        FieldPanel("byyearday"),
        FieldPanel("byeaster"),
        FieldPanel("byweekno"),
        FieldPanel("byweekday"),
    ]

    def __str__(self):
        return f"{self.name} from {self.start_time} to {self.end_time}"
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
