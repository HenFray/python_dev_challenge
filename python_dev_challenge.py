import requests


class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        requests_weather_pehuajo = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(GeoAPI.LAT, GeoAPI.LON, GeoAPI.API_KEY))
        # https://api.openweathermap.org/data/2.5/weather?lat=-35.836948753554054&lon=-61.870523905384076&appid=d81015613923e3e435231f2740d5610b
        # if requests_weather_pehuajo.status_code=="200":
        try:
            response_weather_pehuajo = requests_weather_pehuajo.json()

            main_temps = response_weather_pehuajo["main"]
            temp_actually = main_temps["temp"]

            # 301.15 Kelvin = 28 celsius 
            if temp_actually>301.15:
                return True

            else:
                return False

        except:
            return False







if __name__ == "__main__":

    print(GeoAPI.is_hot_in_pehuajo())
    