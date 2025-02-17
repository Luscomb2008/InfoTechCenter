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


def gaslevelalert():
    milesToGasStationLow = round(random.uniform(1,25,),1)
    milesToGasStationQaurter = round(random.uniform(25.1,50),1)
    
    
    gaslevelindicator = GasLevelGauge()
    if gaslevelindicator == "Empty":
        print("\n\n******WARNING******  YOU ARE OUT OF GAS\n\n")
        sleep(1.25)
        print("\n\ncalling AAA...\n")
    elif gaslevelindicator == "Low":
        print("\nYour gas tank is extremly low, using gps for the closest gas station...\n")
        sleep(1.25)
        print("\nthe closes gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.\n")
    elif gaslevelindicator == "Qaurter tank":
        print("\nYour gas tank is at a qaurter tank, using gps for the closest gas station...\n")
        sleep(1.25)
        print("\nthe closes gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.\n")
    elif gaslevelindicator == "Half Tank":
        print("\nYour gas tank is at a Half Tank, which is plenty to get to your destination!\n")
        sleep(1.25)
    elif gaslevelindicator == "Three-Quarter tank":
        print("\nYour gas tank is at a Three-Quarter tank, which is plenty to get to your destination!\n")
        sleep(1.25)
    else:
        print("\nYour gas tank is at a Full tank, which is Perfect! Go hit the Drag Strip!!\n")
        
        


gaslevelalert()







