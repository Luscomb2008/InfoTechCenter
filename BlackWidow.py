print("\n*******************************************\n")
print("Gasoline Branch - Developer : Lucas Luscomb")

import random 
from time import sleep

def GasLevelGauge():
  GasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three-Quarter tank", "Full tank"]
  return random.choice(GasLevelList)

print(GasLevelGauge())
