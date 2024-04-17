import requests
import json
import pyttsx3
import os

engine = pyttsx3.init()

os.system("cls")
engine.say("Welcome to Weather Application.")
print("Welcome to Weather Application.")
engine.runAndWait()

city = input("Enter name of City : ")
url = f"https://api.weatherapi.com/v1/current.json?key=1df95bc8d89d44aa85994748241704&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
print("All data has been fatched.")
while True:
    os.system("cls")
    print("1 : Check Temperature")
    print("2 : Check Wind Speed")
    print("3 : Check Humidity")
    print("4 : Check Weather Condition")
    print("5 : Exit")
    choice = int(input("What is Your Choice : "))
    if choice == 1:
        current_temperature = wdic["current"]["temp_c"]
        print(f"In {city} city has {current_temperature} degree celcius.")
        engine.say(f"In {city} city has {current_temperature} degree celcius.")
        engine.runAndWait()
    if choice == 2:
        windspeed = wdic["current"]["wind_kph"]
        print(f"In {city} city has {windspeed} km/h wind speed.")
        engine.say(f"In {city} city has {windspeed} km/h wind speed.")
        engine.runAndWait()
    if choice == 3:
        humidity = wdic["current"]["humidity"]
        print(f"In {city} city has {humidity} % humidity.")
        engine.say(f"In {city} city has {humidity} % humidity.")
        engine.runAndWait()

    if choice == 4:
        condition = wdic["current"]["condition"]["text"]
        print(f"In {city} city has {condition} weather condition.")
        engine.say(f"In {city} city has {condition} weather condition.")
        engine.runAndWait()
    if choice == 5:
        print("Perfom Exit")
        engine.say("Perfom Exit")
        engine.runAndWait()
        break
