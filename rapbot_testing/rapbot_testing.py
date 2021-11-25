import time
import os

# establish list of names
names = [str("cherry"), str("billy"), str("rose")]

# initiate game / rules
time.sleep(3)
choosing_name = str(input("Enter your name: "))

# check string with input // data
for x in names:
    if choosing_name in names:
        time.sleep(1)
        print("..." + "processing data...")
        time.sleep(2)
        print("Please wait. ")
        time.sleep(3)
        print("Name chosen. ")
        time.sleep(1)
    break

# battle starts
time.sleep(1)
print("You wanna rhyme against me? ")
time.sleep(2)
print("Let's see, what you got!")
time.sleep(2)
print("Are ")
time.sleep(1)
print("you ")
time.sleep(1)
print("READY? ")

# write a timer / counter
time.sleep(2)
print("Let's go in..." + "3" + "..." )
time.sleep(1)
print("Let's go in..." + "2" + "...")
time.sleep(1)
print("Let's go in..." + "1" + "...")

# clear counting in program
# os.system("clear")

# building syntax
time.sleep(1)
pronouns = (str("he"), str("she"), str("it"))
verbs = (str("does"), str("rhymes"), str("lies"))
adjectives = (str("big"), str("small"), str("tough"))

syntax01 = [pronouns, verbs, adjectives]

# creating loops for Syntax01
for i in syntax01:
    if i in syntax01:
        print(pronouns[0:1])
        print(verbs[0:1])
        print(adjectives[0:1])
    break

# separate the rhyme
print(", ")

# creating second syntax
pronouns2 = (str("he"), str("she"), str("it"), str("they"))
verbs2 = (str("think"), str("drink"), str("blink"))
adjectives2 = (str("great"), str("greedy"), str("fast"))

syntax02 = [pronouns2, verbs2, adjectives2]

# creating loop2 for syntax02
for i in syntax02:
    if i in syntax02:
        print(pronouns2[0:1])
        print(verbs2[0:1])
        print(adjectives2[0:1])
    break

print(", ")

# this is the code for 2 bars.
# aim for the next session
# create an input function call, through which the player can interact with the bot
# 1st option: player presses one word into the call and bot gives a word back
# 2nd option: bot rhymes one rhyme and the player has to complete the rhyme line
# next step is to modify code in def functions / f.e. def syntax01 (): ...
# how can i merge the rhyme lines into one rhyme line again
# create a timer function
