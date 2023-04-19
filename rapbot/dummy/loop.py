import time
import nltk
from os import system, name
import sys
import collections
from nltk.tokenize import word_tokenize

def intro():
    while True:
        names = ["cherry", "fearless", "rose"]
        print(names)

        select = input("Enter your name: ")
        for select in names:
            if select in names:
                print("Success!")
                break
intro()

def exit():
    if select in names:
        print("Success!")
        simulation()

exit()
