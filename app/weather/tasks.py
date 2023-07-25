from datetime import datetime
import pytz

from celery.utils.log import get_task_logger

from consort.celery import transaction_task_with_retry
from weather.models import AirQuality, Forecast


logger = get_task_logger(__name__)


@transaction_task_with_retry()
def update_weather():
    Forecast.objects.all().delete()

    api_key = "b0010b6edcd2188e882720f6a70283c8"
    lat = "52.0168"
    lon = "-110.7684"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric&exclude='minutely,hourly'"

    import requests
    import json
    response = requests.get(url)

    if (response.status_code != 200):
        logger.error('Issue communicating with weather API')
        response.raise_for_status() 

    data = json.loads(response.text)   
    
    daily = data["daily"]
    for i, entry in enumerate(daily):
        Forecast.objects.create(
            forecast_index = i+1,
            date = datetime.fromtimestamp(entry["dt"], pytz.timezone('America/Edmonton')).date(),
            high_temperature = round(entry["temp"]["max"]),
            low_temperature = round(entry["temp"]["min"]),
            main = entry["weather"][0]["main"],
            description = entry["weather"][0]["description"],
            icon_id = entry["weather"][0]["icon"],
        )
    
    current_forecast = data["current"]
    Forecast.objects.create(
            forecast_index = 0,
            date = datetime.fromtimestamp(current_forecast["dt"], pytz.timezone('America/Edmonton')).date(),
            main = current_forecast["weather"][0]["main"],
            description = current_forecast["weather"][0]["description"],
            icon_id = current_forecast["weather"][0]["icon"],
            current_temperature = round(current_forecast["temp"])
    )

    logger.info('Weather updated successfully')


@transaction_task_with_retry()
def update_aqi():

    def calculate_aqi(pm25):
        if pm25 < 0:
            return -1
        elif pm25 <= 12:
            return round(50/12 * pm25)
        elif pm25 <= 35.4:
            return round(49/23.4 * (pm25 - 12) + 51)
        elif pm25 <= 55.4:
            return round(49/19.9 * (pm25 - 35.4) + 101)
        elif pm25 <= 150.4:
            return round(49/94.9 * (pm25 - 55.4) + 151)
        elif pm25 <= 250.4:
            return round(49/99.9 * (pm25 - 150.4) + 201)
        elif pm25 <= 350.4:
            return round(49/99.9 * (pm25 - 250.4) + 301)
        elif pm25 <= 500.4:
            return round(49/149.9 * (pm25 - 350.4) + 401)
        else:
            return -1

    AirQuality.objects.all().delete()

    sensor_index = "122099"
    url = f"https://api.purpleair.com/v1/sensors/{sensor_index}?fields=pm2.5,pm2.5_10minute,pm2.5_30minute,pm2.5_60minute,pm2.5_6hour,pm2.5_24hour,pm2.5_1week"
    headers = { "X-API-Key" : "407BF525-2B0E-11EE-A77F-42010A800009" }
    import requests
    import json

    response = requests.get(url, headers=headers)

    if (response.status_code != 200):
        logger.error('Issue communicating with air quality API')
        response.raise_for_status() 

    data = json.loads(response.text)
    
    sensor_data = data["sensor"]["stats"]

    if  calculate_aqi(sensor_data["pm2.5"]) >= 0 and \
        calculate_aqi(sensor_data["pm2.5_10minute"]) >= 0 and \
        calculate_aqi(sensor_data["pm2.5_30minute"]) >= 0 and \
        calculate_aqi(sensor_data["pm2.5_60minute"]) >= 0 and \
        calculate_aqi(sensor_data["pm2.5_6hour"]) >= 0 and \
        calculate_aqi(sensor_data["pm2.5_24hour"]) >= 0 and \
        calculate_aqi(sensor_data["pm2.5_1week"]) >= 0:
        AirQuality.objects.create(
            datetime = datetime.fromtimestamp(data["data_time_stamp"], pytz.timezone('America/Edmonton')),
            current = calculate_aqi(sensor_data["pm2.5"]),
            avg_10minute = calculate_aqi(sensor_data["pm2.5_10minute"]),
            avg_30minute = calculate_aqi(sensor_data["pm2.5_30minute"]),
            avg_60minute = calculate_aqi(sensor_data["pm2.5_60minute"]),
            avg_6hour = calculate_aqi(sensor_data["pm2.5_6hour"]),
            avg_24hour = calculate_aqi(sensor_data["pm2.5_24hour"]),
            avg_week = calculate_aqi(sensor_data["pm2.5_1week"]),
        )

        logger.info('Air quality updated successfully')
