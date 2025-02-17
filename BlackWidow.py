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
        print("******WARNING******  YOU ARE OUT OF GAS\n")
        sleep(1.25)
        print("calling AAA")
    elif gaslevelindicator == "Low":
        print("Your gas tank is extremly low, using gps for the closest gas station...")
        sleep(1.25)
        print("the closes gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gaslevelindicator == "Low":
        print("Your gas tank is at a qaurter tank, using gps for the closest gas station...")
        sleep(1.25)
        print("the closes gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")

gaslevelalert()







