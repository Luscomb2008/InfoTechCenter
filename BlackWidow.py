print("\n*******************************************\n")
print("Gasoline Branch - Developer : Lucas Luscomb")

import random 
from time import sleep

def GasLevelGauge():
    GasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three-Quarter tank", "Full tank"]
    return random.choice(GasLevelList)

def gasStations():
    gasStationsList = ["Shell", "Marathon", "Circle K", "Wesco", "Buc-ee's", "Meijer",]
    return random.choice(gasStationsList)


print(GasLevelGauge())
print(gasStations())




