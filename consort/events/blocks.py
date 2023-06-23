from django.core.exceptions import ValidationError

from wagtail import blocks


class Timespan(blocks.StructBlock):
    start_time = blocks.DateTimeBlock(
        required=True,
        help_text='The date and time the event starts',
    )
    
    end_time = blocks.DateTimeBlock(
        required=True,
        help_text='The date and time the event ends',
    )

    def clean(self, value):
        result = super().clean(value)
        if result["start_time"] > result["end_time"]:
            raise ValidationError("End time must come after start time")
        return result
