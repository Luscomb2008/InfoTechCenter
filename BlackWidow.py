print("\n*****************************************\n")

print("Weather Branch - Developer: Lucas Luscomb\n")

#Import Libraries Here!
import random
from time import sleep

#Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert= weather()

def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe Nation Weather Service has updated our alarm by 30 minutes because"
            "of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("\nThe Nation Weather Service has updated our alarm by 60 minutes because"
            "of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "icy":
        print("\nThe Nation Weather Service has updated our alarm by 60 minutes because"
            "of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "rainy":
        print("\nThe Nation Weather Service has updated our alarm by 10 minutes because"
            "of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "windy":
        print("\nThe Nation Weather Service has updated our alarm by 5 minutes because"
            "of the forecast of", weatherAlert, "outside.")
    elif weatherAlert == "sunny":
        print("\nThe Nation Weather Service has predicted"
            " the forecast of", weatherAlert, "outside.")



vehicleResponseSystem()