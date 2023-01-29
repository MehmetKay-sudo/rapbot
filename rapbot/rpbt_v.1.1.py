import time
from os import system
import random

# START // INITIALISATION-----------------------------------------------------------------------------------------------
# establish list of names
names = [str("cherry"), str("fearless"), str("rose")]
time.sleep(1)
print(str(names))

# make user choose name
time.sleep(3)
choosing_name = str(input("Enter your name: "))

###############
# flush display
system("clear")
###############

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

###############
# flush display
system("clear")
###############

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

###############
# flush display
system("clear")
###############

# write a timer / counter
time.sleep(2)
print("Let's go in..." + "3" + "..." )
time.sleep(1)
print("Let's go in..." + "2" + "...")
time.sleep(1)
print("Let's go in..." + "1" + "...")

###############
# flush display
system("clear")
###############

# RAP BATTLE // ACTUAL ENCOUNTER----------------------------------------------------------------------------------------
# 1ST ROUND OF BATTLE
# building syntax
bar1 = str("I rhyme fine!")
bar2 = str("I rhyme great!")
bar3 = str("I am the best in the state!")

# mix 1st round syntax
syntax_bot = [str(bar1), str(bar2), str(bar3)]

# creating loops for Syntax01
for y in syntax_bot:
    if y in syntax_bot:
        time.sleep(1)
        print(bar1)
        time.sleep(1)
        print(bar2)
        time.sleep(1)
        print(bar3)
    break

# print the options the rhymer has / 1st round
rhyme01 = str("1. I am greater! ")
rhyme02 = str("2. I rhyme great! ")
rhyme03 = str("3. You ain't a saint, the worst in the state!")

player_rhymes = (str(rhyme01), str(rhyme02), str(rhyme03))
print(player_rhymes)

# player has to put input into the game
time.sleep(1)
rhyme_user = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for z in syntax_bot:
    if rhyme_user == rhyme01:
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))
    else:
        print(False)
        break

    if rhyme_user == rhyme02:
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))
    else:
        print(False)
        break

    if rhyme_user == rhyme03:
        print("AAAAAAHHHHHH! ")
        time.sleep(1)
        print("You beat me once" + ", " + "Let's see, what you will do in the next round! ")
        time.sleep(5)
        print(True)
    break

###############
# flush display
system("clear")
###############


# 2ND ROUND OF BATTLE---------------------------------------------------------------------------------------------------
# creating second syntax
bar4 = str("I am straight! ")
bar5 = str("Big my brain! ")
bar6 = str("Skilled and insane! ")

syntax_bot2 = [str(bar4), str(bar5), str(bar6)]

# creating loop2 for syntax02
for i in syntax_bot2:
    if i in syntax_bot2:
        time.sleep(1)
        print(bar4)
        time.sleep(2)
        print(bar5)
        time.sleep(3)
        print(bar6)
    break

# print the options the rhymer has
rhyme04 = str("1. You are late! ")
rhyme05 = str("2. Big my brain! ")
rhyme06 = str("3. You just faint and i maintain! ")

player_rhymes = (str(rhyme04), str(rhyme05), str(rhyme06))
print(player_rhymes)

# player has to put input into the game
time.sleep(1)
rhyme_user2 = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for i in syntax_bot2:
    if rhyme_user2 == rhyme04:
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))
    else:
        print(False)
        break

    if rhyme_user == rhyme05:
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))
    else:
        print(False)
        break

    if rhyme_user == rhyme06:
        print("You beat me twice, let us see next round")
    break

###############
# flush display
system("clear")
###############

# RAP BATTLE // ACTUAL ENCOUNTER----------------------------------------------------------------------------------------
# 3ST ROUND OF BATTLE / LAST MAN STANDING
time.sleep(2)
print("This is the last round sucker! Show me your skills! ")

# building syntax
bar7 = str("Killer instinct. ")
bar8 = str("Kill you with one ink. ")
bar9 = str("Don't try me, otherwise you go exstinct. ")

# mix 1st round syntax
syntax_bot3 = [str(bar7), str(bar8), str(bar9)]

# creating loops for Syntax01
for y in syntax_bot3:
    if y in syntax_bot3:
        time.sleep(1)
        print(bar7)
        time.sleep(1)
        print(bar8)
        time.sleep(1)
        print(bar9)
    break

# print the options the rhymer has
rhyme07 = str("1. I am greater! ")
rhyme08 = str("2. Kill you with one ink. ")
rhyme09 = str("3. You fake n-sync, i terminate before an eye blink! ")

player_rhymes = (str(rhyme07), str(rhyme08), str(rhyme09))
print(player_rhymes)

# player has to put input into the game
time.sleep(1)
rhyme_user3 = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for b in syntax_bot3:
    if rhyme_user == rhyme07:
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))
    else:
        print(False)
        break

    if rhyme_user == rhyme08:
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))
    else:
        print(False)
        break

    if rhyme_user == rhyme09:
        time.sleep(2)
        print("AAAAAAHHHHHH! ")
        time.sleep(1)
        print("You won! "+ ", " + "Let me mourn my defeat rap-samurai! ")
        time.sleep(5)
        print("Game ends...")
        time.sleep(1)
        print("MIXTAPE GAMES / 2021")
    break

###############
# flush display
system("clear")
###############
