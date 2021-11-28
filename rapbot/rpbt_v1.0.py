import time
import os
# START // INITIALISATION-----------------------------------------------------------------------------------------------
# establish list of names
names = [str("cherry"), str("fearless"), str("rose")]
time.sleep(1)
print(str(names))
# initiate game / rules
time.sleep(3)
choosing_name = str(input("Enter your name: "))

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
# clear what was written before
# os.system("clear")

# RAP BATTLE // ACTUAL ENCOUNTER----------------------------------------------------------------------------------------
# 1ST ROUND OF BATTLE
# building syntax
bar1 = str("I rhyme fine!")
bar2 = str("I rhyme great!")
bar3 = str("I am the best in the state!")

# mix 1st round syntax
syntax_bot = [bar1, bar2, bar3]

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

# player has to put input into the game
time.sleep(1)
rhyme_user = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for z in syntax_bot:
    if rhyme_user == "I am greater":
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))

    if rhyme_user == bar2:
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))

    if rhyme_user == "You ain't a saint, the worst in the state! ":
        print("AAAAAAHHHHHH! ")
        time.sleep(1)
        print("You beat me once" + ", " + "Let's see, what you will do in the next round! ")
        time.sleep(5)
    break

# built-in return

# 2ND ROUND OF BATTLE---------------------------------------------------------------------------------------------------
# creating second syntax
bar4 = str("I am straight! ")
bar5 = str("Big my brain! ")
bar6 = str("Skilled and insane! ")

syntax_bot2 = [bar4, bar5, bar6]

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

# player has to put input into the game
time.sleep(1)
rhyme_user2 = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for i in syntax_bot2:
    if rhyme_user2 == "You are late ":
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))

    if rhyme_user == "Big my brain! ":
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))

    if rhyme_user == "You just faint and i maintain! ":
        print("You beat me twice, let us see next round")
    break

# RAP BATTLE // ACTUAL ENCOUNTER----------------------------------------------------------------------------------------
# 3ST ROUND OF BATTLE / LAST MAN STANDING
time.sleep(2)
print("This is the last round sucker! Show me your skills! ")

# building syntax
bar7 = str("Killer instinct.")
bar8 = str("Kill you with one ink.")
bar9 = str("Don't try me, otherwise you go exstinct.")

# mix 1st round syntax
syntax_bot3 = [bar7, bar8, bar9]

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

# player has to put input into the game
time.sleep(1)
rhyme_user3 = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for b in syntax_bot3:
    if rhyme_user == "I am greater":
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))

    if rhyme_user == bar2:
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
        time.sleep(1)
        print(str(input("Enter your rhyme sucker: ")))

    if rhyme_user == "You ain't a saint, the worst in the state! ":
        time.sleep(2)
        print("AAAAAAHHHHHH! ")
        time.sleep(1)
        print("You won! "+ ", " + "Let me mourn my defeat rap-samurai! ")
        time.sleep(5)
        print("Game ends...")
    break



