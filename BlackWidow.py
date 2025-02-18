import random
from time import sleep

def gas_level_alert():
    levels = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three-Quarter tank", "Full tank"]
    stations = ["Shell", "Marathon", "Circle K", "Wesco", "Buc-ee's", "Meijer"]
    level = random.choice(levels)
    station, miles = (random.choice(stations), round(random.uniform(1, 50), 1)) if level in ["Low", "Quarter tank"] else (None, 0)

    sleep(1.25)
    print(f"\nGas Level: {level}")
    if level == "Empty": print("\n******WARNING******  YOU ARE OUT OF GAS\n\nCalling AAA...\n")
    else: print(f"The closest gas station is {station}, {miles} miles away." if miles else "Your gas level is enough to reach your destination.")

gas_level_alert()


