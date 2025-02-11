import random
from time import sleep

# Streamlined dictionary for weather response
weather_responses = {
    "snowing": (30, "engaged, limiting speed to 55MPH"),
    "blizzard": (60, "engaged, limiting speed to 55MPH"),
    "icy": (60, "engaged, limiting speed to 35MPH"),
    "rainy": (10, "disengaged"),
    "windy": (5, "disengaged"),
    "sunny": (0, "disengaged"),
}

def vehicleResponseSystem():
    # Choose the weather condition and print the response in one step
    alert, (delay, vrs_status) = random.choice(list(weather_responses.items()))
    print(f"\nThe National Weather Service has updated our alarm by {delay} minutes "
          f"because of the forecast of {alert} outside.")
    sleep(1)  # Adding a slight delay for realism
    print(f"VRS has been {vrs_status}.")

# Main driver function
if __name__ == "__main__":
    print("\n*****************************************\n")
    print("Weather Branch - Developer: Lucas Luscomb")
    vehicleResponseSystem()
