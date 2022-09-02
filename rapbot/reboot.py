import time
#from os import system
import random

# START // INITIALISATION-SIMULATION----------------------------------------------------------------------------------------------
# establish list of names
while True:
    names = [("cherry", "fearless", "rose")]
    time.sleep(1)
    for k in names:
        print(names)

# make user choose name
    time.sleep(3)
    choosing_name = input("Enter your name: ")

# check string with input // data
    for x in names:
        if choosing_name in names:
            time.sleep(1)
            print("." + "." + "." + "processing data" + "." + "." + ".")
            time.sleep(2)
            print("Please wait. ")
            time.sleep(3)
            print("Name chosen. ")
            time.sleep(1)
        break
