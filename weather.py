import requests

api_url = "https://api.openweathermap.org/data/2.5/weather"
key = "09a0b8dee865e78eab58dfe6c243b043"

city = input("City? ")

params = {
    'q': city,  # Saint Petersburg,ru',
    'appid': '09a0b8dee865e78eab58dfe6c243b043',
    # 'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric',
    'lang': 'ru'
}


res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers["Content-Type"])
data = res.json()
print(f"Current temperature in {city} is {data['main']['temp']} \u2103, {data['weather'][0]['description']}")
