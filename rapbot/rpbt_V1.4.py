import time
from os import system, name
#import random

# all bars are examples and can be modified
# START // INITIALISATION-SIMULATION
# establish list of names
class Intro:
    names = [("cherry", "fearless", "rose")]
    print(names)
    choosing_name = input("Enter your name: ")
    if choosing_name in names:
        print(choosing_name)
#        break
# here will be code to exit() program
# check string with input // data
    def simulation():
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

simulation1 = simulation()
print(simulation1)

#  flushing the screen
# def clear():

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
    # write a timer / counter
def simulation3():
        time.sleep(2)
        print("Let's go in..." + "3" + "..." )
        time.sleep(1)
        print("Let's go in..." + "2" + "...")
        time.sleep(1)
        print("Let's go in..." + "1" + "...")
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
                # creating loops for barsdef bars_loop()
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
                # compare rhyme from user with syntax from bot
            def compare():
                for z in syntax_bot:
                    if rhyme_user == rhyme01:
                        print("Nice try fella! ")
                        print("Try again! ")
                        print(str(input("Enter your rhyme sucker: ")))
                    else:
                        print(False)
                        return()
                    if rhyme_user == rhyme02:
                        print("Why are you telling the same thing, as i do? ")
                        print("Try again! ")
                        print(str(input("Enter your rhyme sucker: ")))
                    else:
                        print(False)
                        break
                    if rhyme_user == rhyme03:
                        print("AAAAAAHHHHHH! ")
                        print("You beat me once" + ", " + "Let's see, what you will do in the next round! ")
                        print(True)
                        break
    # 2nd ROUND OF BATTLE
    class Round2:
        while True:
            def bars2():
                bar4 = str("I am straight! ")
                bar5 = str("Big my brain! ")
                bar6 = str("Skilled and insane! ")
                syntax_bot2 = [str(bar4), str(bar5), str(bar6)]
                print(syntax_bot2)
            # creating loop2 for syntax02
            def bars_loop2():
                for i in syntax_bot2:
                    if i in syntax_bot2:
                        print(bar4)
                        print(bar5)
                        print(bar6)
                    break
            # print the options the rhymer has
            def options2():
                rhyme04 = str("1. You are late! ")
                rhyme05 = str("2. Big my brain! ")
                rhyme06 = str("3. You just faint and i maintain! ")
                player_rhymes = (str(rhyme04), str(rhyme05), str(rhyme06))
                print(player_rhymes)
                # player has to put input into the game
                rhyme_user2 = str(input("Enter your rhyme sucker: "))
                # compare rhyme from user with syntax from bot
            def compare2():
                for i in syntax_bot2:
                    if rhyme_user2 == rhyme04:
                        print("Nice try fella! ")
                        print("Try again! ")
                        print(str(input("Enter your rhyme sucker: ")))
                    else:
                        print(False)
                    break
                    if rhyme_user == rhyme05:
                        print("Why are you telling the same thing, as i do? ")
                        print("Try again! ")
                        print(str(input("Enter your rhyme sucker: ")))
                    else:
                        print(False)
                        break
                    if rhyme_user == rhyme06:
                        print("You beat me twice, let us see next round")
                        break
    class Round3:
        while True:
            def bars3():
                bar7 = str("Killer instinct. ")
                bar8 = str("Kill you with one ink. ")
                bar9 = str("Don't try me, otherwise you go exstinct. ")
                # mix 1st round syntax
                syntax_bot3 = [str(bar7), str(bar8), str(bar9)]
                print(syntax_bot3)
                # creating loops
            def bars_loop3():
                for y in syntax_bot3:
                    print(bar7)
                    print(bar8)
                    print(bar9)
                    break
                    # print the options the rhymer has
            def options3():
                rhyme07 = str("1. I am greater! ")
                rhyme08 = str("2. Kill you with one ink. ")
                rhyme09 = str("3. You fake n-sync, i terminate before an eye blink! ")
                player_rhymes = (str(rhyme07), str(rhyme08), str(rhyme09))
                print(player_rhymes)
                # player has to put input into the game
                rhyme_user3 = str(input("Enter your rhyme sucker: "))
                # compare rhyme from user with syntax from bot
            def compare3():
                for b in syntax_bot3:
                    if rhyme_user == rhyme07:
                        print("Nice try fella! ")
                        print("Try again! ")
                        print(str(input("Enter your rhyme sucker: ")))
                    else:
                        print(False)
                        break
                    if rhyme_user == rhyme08:
                        print("Why are you telling the same thing, as i do? ")
                        print("Try again! ")
                        print(str(input("Enter your rhyme sucker: ")))
                    else:
                        print(False)
                        break
                    if rhyme_user == rhyme09:
                        print("AAAAAAHHHHHH! ")
                        print("You won! "+ ", " + "Let me mourn my defeat rap-samurai! ")
                    break
