# Print initial lines with some separation and title
print("\n*****************************************\n")
print("Weather Branch - Developer: Lucas Luscomb")

# Import necessary libraries
import random  # For generating random weather conditions
from time import sleep  # For creating time delays (though not used in the code)

# Weather Function to determine the weather condition randomly
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    # Randomly choose one weather condition from the list
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition  # Return the selected weather condition

# Call the weather function to get a random weather alert
weatherAlert = weather()

# Define the vehicle response system that reacts to different weather conditions
def vehicleResponseSystem():
    # Check different weather conditions and print corresponding messages
    if weatherAlert == "snowing":
        print("\nThe Nation Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55MPH.")
    elif weatherAlert == "blizzard":
        print("\nThe Nation Weather Service has updated our alarm by 60 minutes because"
              " of the forecast of", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55MPH.")
    elif weatherAlert == "icy":
        print("\nThe Nation Weather Service has updated our alarm by 60 minutes because"
              " of the forecast of", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 35MPH.")
    elif weatherAlert == "rainy":
        print("\nThe Nation Weather Service has updated our alarm by 10 minutes because"
              " of the forecast of", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been disengaged.")
    elif weatherAlert == "windy":
        print("\nThe Nation Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been disengaged.")
    elif weatherAlert == "sunny":
        print("\nThe Nation Weather Service has predicted"
              " the forecast of", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been disengaged.")

# Call the vehicle response system to output the alarm update based on the current weather
vehicleResponseSystem()
