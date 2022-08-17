import requests

# register through the following website
# https://openweathermap.org/
# after login on the top-right open tap on arrow beside your name open "my api key "
# copy it
# apikey provided through my website

API_KEY = "132fb3d3977b8c1256cccc437dae4144"

# base url to call and add query parameter to it
BASE_URL = "https://api.openweathermap.org/data/3.0/weather"

# asking for the city you want the weather detail in
city = input("enter your city : ")


params = {'appid': API_KEY, 'q': city}


# request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print("error with the request")
    print(response.status_code)
    print(response)
