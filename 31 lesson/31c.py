'''
Task 3
The Weather app
Write a console application which takes as an input a city name and returns current weather in the format of your choice.
For the current task, you can choose any weather API or website or use https://openweathermap.org 
'''

# [https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/]

import requests
import json


api_key = "Your_API_Key"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")


if __name__ == '__main__':
    pass

'''
---output---

'''
