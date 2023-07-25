from django.db import models

class Forecast(models.Model):
    date = models.DateField(
        null=True,
        help_text="The day when the forecasted weather occurs"
    )

    main = models.CharField(
        max_length=20,
        help_text="The type of weather (rain, snow, etc.)"
    )

    description = models.CharField(
        max_length=30,
        help_text="A description of the weather"
    )

    icon_id = models.CharField(
        max_length=3,
        help_text="The id of the icon"
    )

    forecast_index = models.IntegerField()
    high_temperature = models.IntegerField(null=True)
    low_temperature = models.IntegerField(null=True)
    current_temperature = models.IntegerField(null=True)


class AirQuality(models.Model):
    datetime = models.DateTimeField(
        null=True,
        help_text="The time when the air quality measurement was taken"
    )

    current = models.FloatField()
    avg_10minute = models.FloatField()
    avg_30minute = models.FloatField()
    avg_60minute = models.FloatField()
    avg_6hour = models.FloatField()
    avg_24hour = models.FloatField()
    avg_week = models.FloatField()
