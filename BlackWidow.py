# Import necessary libraries
import sys  # Provides access to system-specific parameters and functions
import time  # Provides time-related functions
import random
from time import sleep



# ANSI escape sequences for colors (Rainbow effect)
RESET = "\033[0m"  # Reset color
RED = "\033[31m"   # Red color
GREEN = "\033[32m" # Green color
YELLOW = "\033[33m" # Yellow color
BLUE = "\033[34m"  # Blue color
MAGENTA = "\033[35m" # Magenta color
CYAN = "\033[36m"  # Cyan color
WHITE = "\033[37m" # White color

# List of colors for the rainbow effect
colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]

# Print the welcome message and developer info in a rainbow color
print(f"{CYAN}Welcome Branch - Developer: Lucas Luscomb{RESET}")

# Print a greeting message for InfoTechCenter in a random rainbow color
print(f"\n\t{colors[0]}Welcome To InfoTechCenter!{RESET}\n")

# Initialize variables
x = 0  # Counter to track the number of iterations
ellipsis = 0  # Variable to control the number of dots in the loading message
color_index = 0  # To cycle through the colors list

# Start a loop that runs 20 times
while x != 20:
    x += 1  # Increment counter
    # Create a message with a varying number of dots and apply a rainbow color
    message = f"{colors[color_index]}InfoTech Center System Booting{RESET}" + "." * ellipsis
    ellipsis += 1  # Increase the number of dots
    
    # Overwrite the previous output on the same line with the new message
    sys.stdout.write(f"\r{message}")
    
    # Pause for half a second before updating the message
    time.sleep(.5)
    
    # Reset the number of dots after reaching 4
    if ellipsis == 4:
        ellipsis = 0
    
    # Cycle through the rainbow colors
    color_index = (color_index + 1) % len(colors)
    
    # Once the loop reaches 20 iterations, print a final success message in green
    if x == 20:
        print(f"\n\n{GREEN}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")

# Comments below will also be rainbow-colored!

# This part of the script deals with the loop for booting system process
# The loop runs 20 iterations, and every time it does, the message color changes
# The number of dots in the "booting" message increases up to 4, then resets

# The color of the final success message is set to Green to highlight the completion

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

import random  # Import the random module to generate random values






