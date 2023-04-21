import time
import nltk
import sys
import collections
import nltk
from nltk.tokenize import word_tokenize


def main():
    intro()
    simulation1()
    simulation2()
    simulation3()
    bars()
    options()
    compare()
    bars2()
    bars_loop()
    option2()
    compare2()
    bars3()
    bars_loop2()
    options3()
    compare3()


# all bars are examples and can be modified
# START // INITIALISATION-SIMULATION
# establish list of names
# need to debug here
# program does not fully proceed

def intro():
    while True:
        name = [("cherry", "fearless", "rose")]
        print(name)

        select = input("Enter your name: ")
        for select in name:
            if select in name:
                print("Battlename successfully selected")
            else:
                intro()
        break


intro()

# flush the screen after intro
# os.system('clear')

# check string with input
def simulation1():
    for select in name:
        if select in name:
            time.sleep(1)
            dot = "."
            print(dot * 3 + "processing data" + dot * 3)
            time.sleep(2)
            print("Please wait. ")
            time.sleep(3)
            print("Name chosen. ")
            time.sleep(1)
            break


simulation1()

# flushing the screen again
# os.system('clear')

# battle starts
def simulation2():
    print("You wanna rhyme against me? ")
    print("Let's see, what you got!")
    time.sleep(2)
    print("Are ")
    time.sleep(1)
    print("you ")
    time.sleep(1)
    print("READY? ")


simulation2()


def simulation3():
    time.sleep(2)
    print("Let's go in..." + "3" + "...")
    time.sleep(1)
    print("Let's go in..." + "2" + "...")
    time.sleep(1)
    print("Let's go in..." + "1" + "...")


simulation3()

# program stuck here
# RAP BATTLE // ACTUAL ENCOUNTER
# 1st ROUND OF BATTLE


class Battle:
    class Round1:
        while True:
            def bars():
                bar1 = str("I rhyme fine!")
                bar2 = str("I rhyme great!")
                bar3 = str("I am the best in the state!")
                # mix 1st round syntax
                syntax_bot = [str(bar1), str(bar2), str(bar3)]
                print(syntax_bot)
                # creating loops for bars
                def bars_loop():
                    for y in syntax_bot:
                        if y in syntax_bot:
                            print(bar1)
                            print(bar2)
                            print(bar3)
                            break

                # print the options the rhymer has / 1st round
                def options():
                    rhyme01 = str("1. I am greater! ")
                    rhyme02 = str("2. I rhyme great! ")
                    rhyme03 = str("3. You ain't a saint, the worst in the state!")
                    player_rhymes = (str(rhyme01), str(rhyme02), str(rhyme03))
                    print(player_rhymes)
                    # player has to put input into the game
                    time.sleep(1)
                    rhyme_user = str(input("Enter your rhyme sucker: "))
