import time
import nltk
from os import system, name
import sys
import collections
from nltk.tokenize import word_tokenize

# rapbot is starting
def intro():
    while True:
        name = ["cherry", "fearless", "rose"]
        print(name)

        select = input("Enter your name: ")
        for select in name:
            if select in name:
                print("Success!")
            break
        break
intro()

#flushing screen, doesn't work
#os.system('clear')

# rapbot starts talking to user
def simulation():
    for x in name:
        if select in name:
            time.sleep(1)
            dot = "."
            print(dot*3 + "processing data" + dot*3)
            time.sleep(2)
            print("Please wait. ")
            time.sleep(3)
            print("Name chosen. ")
            time.sleep(1)
        break

simulation()
