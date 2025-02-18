import random  # Import the random module to generate random values
from time import sleep  # Import the sleep function from time module to pause execution


# Define the gas_level_alert function
def gas_level_alert():
    # List of possible gas levels and gas stations
    levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three-Quarter tank", "Full tank"]
    stations = ["Shell", "Marathon", "Circle K", "Wesco", "Buc-ee's", "Meijer"]

    # Randomly select a gas level from the list
    level = random.choice(levels)

    # If the level is "Low" or "Quarter Tank", select a random station and calculate distance to it
    # Otherwise, no station is needed and miles is set to 0
    station, miles = (random.choice(stations), round(random.uniform(1, 50), 1)) if level in ["Low",
                                                                                             "Quarter tank"] else (
    None, 0)

    sleep(1.25)  # Pause the program for 1.25 seconds to simulate processing time

    # Print the current gas level
    print(f"\nGas Level: {level}")

    # If the gas level is "Empty", print a warning and simulate a call to AAA
    if level == "Empty":
        print("\n******WARNING******  YOU ARE OUT OF GAS\n\nCalling AAA...\n")
    else:
        # If there is a station and miles, print the closest station and its distance
        # If no station is needed, inform the user that their gas level is enough
        print(
            f"The closest gas station is {station}, {miles} miles away." if miles else "Your gas level is enough to reach your destination.")


# Call the gas_level_alert function to execute the program
gas_level_alert()

