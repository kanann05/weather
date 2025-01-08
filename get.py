import requests

def get_weather_data(city):
    api_key = "ba20ff65b7f35f641cffd7012c207642"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q" : city,
        "APPID" : api_key,
        "units" : "metric"
    }
    response = requests.get(url, params)
    if(response.status_code == 200):
        return response.json()
    else:
        return None
