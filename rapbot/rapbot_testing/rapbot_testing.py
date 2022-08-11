import time
import os
# START // INITIALISATION-----------------------------------------------------------------------------------------------
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

# RAP BATTLE // ACTUAL ENCOUNTER----------------------------------------------------------------------------------------
# 1ST ROUND OF BATTLE
# building syntax
time.sleep(1)
pronouns = (str("he"), str("she"), str("it"))
verbs = (str("does"), str("rhymes"), str("lies"))
adjectives = (str("big"), str("small"), str("tough"))

# mix 1st round syntax
syntax_bot = [pronouns, verbs, adjectives]

# creating loops for Syntax01
for i in syntax_bot:
    if i in syntax_bot:
        print(pronouns[0:1])
        print(verbs[0:1])
        print(adjectives[0:1])
    break

# player has to put input into the game
rhyme_user = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for i in syntax_bot:
    if rhyme_user == "he is small":
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
    print(rhyme_user)

    if rhyme_user == "he does big":
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
    print(rhyme_user)

    if rhyme_user == "he sucks hard! ":
        print("You beat me once" + ", " + "Let's see, what you will do in the next round! ")
        time.sleep(15)
    break

# 2ND ROUND OF BATTLE---------------------------------------------------------------------------------------------------
# creating second syntax
pronouns2 = (str("he"), str("she"), str("it"), str("they"))
verbs2 = (str("think"), str("drink"), str("blink"))
adjectives2 = (str("great"), str("greedy"), str("fast"))

syntax_bot2 = [pronouns2, verbs2, adjectives2]

# creating loop2 for syntax02
for i in syntax_bot2:
    if i in syntax_bot2:
        print(pronouns2[0:1])
        print(verbs2[0:1])
        print(adjectives2[0:1])
    break

# player has to put input into the game
rhyme_user = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for i in syntax_bot2:
    if rhyme_user == "he is dumb ":
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
    print(rhyme_user)

    if rhyme_user == "he thinks great ":
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
    print(rhyme_user)

    if rhyme_user == "he tries to be smart! ":
        print("You beat me once, let us see next round")
    break





# this is the code for 2 bars.
# aim for the next session
# create an input function call, through which the player can interact with the bot
# 1st option: player presses one word into the call and bot gives a word back
# 2nd option: bot rhymes one rhyme and the player has to complete the rhyme line
# next step is to modify code in def functions / f.e. def syntax01 (): ...
# how can i merge the rhyme lines into one rhyme line again
# create a timer function
