import requests

# stage #1
class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    UNITS= "metric"

    @classmethod
    def is_hot_in_pehuajo(cls):
        requests_weather_pehuajo = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units={}".format(GeoAPI.LAT, GeoAPI.LON, GeoAPI.API_KEY, GeoAPI.UNITS))
        # https://api.openweathermap.org/data/2.5/weather?lat=-35.836948753554054&lon=-61.870523905384076&appid=d81015613923e3e435231f2740d5610b
        try:
            response_weather_pehuajo = requests_weather_pehuajo.json()
            main_temps = response_weather_pehuajo["main"]
            temp_actually = main_temps["temp"]

            if temp_actually>28:
                return True

            else:
                return False

        except:
            return False

if __name__ == "__main__":

    print(GeoAPI.is_hot_in_pehuajo())



