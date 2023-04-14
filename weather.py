# Weather.py 
# AI Weather Skill
# Matt Carmody - April 2023

from pyowm import OWM
from geopy import Nominatim
from datetime import datetime

class Weather():

    #The location of where you want the forecast for
    __location = "Budapest, HU"

    #API Key
    api_key = '90be93527babd2a823f16c364325e6d1'

    def __init__(self):
        self.owm = OWM(self.api_key)
        self.mgr = self.owm.weather_manager()
        locator = Nominatim(user_agent="myGeocoder")
        city = "Budapest"
        country = "HU"
        self.__location = city+ ", "+country
        loc = locator.geocode(self.__location)
        self.lat = loc.latitude
        self.long = loc.longitude


    def uv_index(self, uvi:float):
        """ Returns a message depending on the UV Index provided """
        message = ""
        if float(uvi) <= float(2.0):
            message = "The Ultraviolet level is low, no protection is required."
        if float(uvi) >= 3.0 and float(uvi) <6.0:
            message = "The Ultraviolet level is medium, skin protection is required."
        if float(uvi) >= 6.0 and float(uvi) <8.0:
            message = "The Ultraviolet level is high, skin protection is required."
        if float(uvi) >= 8.0 and float(uvi) <11.0:
            message = "The Ultraviolet level is very high, extra skin protection is required."
        if float(uvi) >= 11.0:
            message = "The Ultraviolet level is extremely high, caution is advised and extra skin protection is required."
        return message
    

    @property
    def weather(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        return forecast
    

    @property
    def forecast(self):
        """Returns the forecast at this location"""
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        detail_status = forecast.forecast_daily[0].detailed_status
        pressure = str(forecast.forecast_daily[0].pressure.get('press'))
        humidity = str(forecast.forecast_daily[0].humidity)
        sunrise = str(datetime.utcfromtimestamp(forecast.forecast_daily[0].sunrise_time()).strftime("%H:%M:%S"))
        sunset = str(datetime.utcfromtimestamp(forecast.forecast_daily[0].sunset_time()).strftime("%H:%M:%S"))
        temperature = str(forecast.forecast_daily[0].temperature('celsius').get('day'))
        uvi = str(forecast.forecast_daily[0].uvi)

        message = "Here is the Weather: Today will be mostly " + detail_status \
                + ", humidity of " + humidity + " percent" \
                + " and a pressure of " + pressure + " millibars" \
                + ". The temperature is " + temperature + "degrees " \
                + ". Sunrise was at " + sunrise \
                + " and sunset is at " + sunset \
                + ". " + self.uv_index(uvi)

        # print(message)
        return message



#demo
myweather = Weather()
print(myweather.forecast)

