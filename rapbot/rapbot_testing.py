import time
from os import system, name
import sys
import collections
#import nltk

def main(self, intro, simulation1, simulation2, simulation3, bars, bars2, bars3, options, option2, options3,
         compare, compare2, compare3, bars_loop, bars_loop2):
  self.intro = intro()
  self.simulation1 = simulation1
  self.simulation2 = simulation2
  self.simulation3 = simulation3
  self.bars = bars
  self.options = options
  self.compare = compare
  self.bars2 = bars2
  self.bars_loop = bars_loop
  self.option2 = option2
  self.compare2 = compare2
  self.bars3 = bars3
  self.bars_loop2 = bars_loop2
  self.options3 = options3
  self.compare3 = compare3

#main = main(self, intro, simulation1, simulation2, simulation3, bars, bars2, bars3, options, option2, options3,
#         compare, compare2, compare3, bars_loop, bars_loop2)
main.intro()
main.simulation1()
main.simulation2()
main.simulation3()
main.bars()
main.simulation2()
main.simulation3()
main.bars()
main.options()
main.compare()
main.bars2()
main.bars_loop()
main.option2()
main.compare2()
main.bars3()
main.bars_loop2()
main.options3()
main.compare3()

# need to place the __init__(self) function
# creat an intro to start the rapbot
class Intro:
  def intro(self, name, name_select, select):
    self.name = name
    self.name_select = name.select
    self.select = select
    name = str("Rapbot")
    name_select = ("cherry", "fearless", "killer", "savage", "beast", "king", "queen", "god", "devil", "angel", "demon", "saint", "sin")
    print(name_select)
    select = input("Enter your name: ")
    if select in name_select:
      print("Battlename successfully selected")
    else:
      print("Invalid name. Try again.")
      print(name_select)
      # check string with input

intro = Intro()
  
  def simulation1(self):
    def intro(self):
      if select in name:
        time.sleep(1)
        dot = "."
        print(dot*3 + "processing data" + dot*3)
        time.sleep(2)
        print("Please wait. ")
        time.sleep(3)
        print("Name chosen. ")
        time.sleep(1)
      # battle starts

simulation1 = simulation1()
  
  def simulation2(self):
    print("You wanna rhyme against me? ")
    print("Let's see what you got!")
    time.sleep(2)
    print("Are you READY? ")
    time.sleep(1)

simulation2 = simulation2()

def simulation3(self):
    time.sleep(2)
    print("Let's go in..." + "3" + "..." )
    time.sleep(1)
    print("Let's go in..." + "2" + "...")
    time.sleep(1)
    print("Let's go in..." + "1" + "...")
    time.sleep(1)

simulation3 = simulation3()

# Round 1 battle module
class Round1:
  round_loop = True
  while round_loop == True:
        def bars(self, bar1, bar2, bar3):
            self.bar1 = bar1
            self.bar2 = bar2
            self.bar3 = bar3
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
        round_loop = False

        # print the options the rhymer has / 1st round
        def options(self, rhyme01, rhyme02, rhyme03):
            rhyme01 = str("1. I am greater! ")
            rhyme02 = str("2. I rhyme great! ")
            rhyme03 = str("3. You ain't a saint, the worst in the state!")
            player_rhymes = (str(rhyme01), str(rhyme02), str(rhyme03))
            print(player_rhymes)
            # player has to put input into the game
            time.sleep(1)
            rhyme_user = str(input("Enter your rhyme sucker: "))

        # compare rhyme from user with syntax from bot
        def compare(self):
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

Round1 = Round1()

# Round2 battle module
class Round2:
  def bars2(self, bar4, bar5, bar6):
    bar4 = str("I am straight! ")
    bar5 = str("Big my brain! ")
    bar6 = str("Skilled and insane! ")
    syntax_bot2 = [str(bar4), str(bar5), str(bar6)]
    print(syntax_bot2)

  # creating loop2 for syntax02
  def bars_loop2(self):
    for i in syntax_bot2:
      if i in syntax_bot2:
        print(bar4)
        print(bar5)
        print(bar6)
        break

  # print the options the rhymer has
  def options2(self, rhyme04, rhyme05, rhyme06, player_rhymes, rhyme_user2):
    rhyme04 = str("1. You are late! ")
    rhyme05 = str("2. Big my brain! ")
    rhyme06 = str("3. You just faint and i maintain! ")
    player_rhymes = (str(rhyme04), str(rhyme05), str(rhyme06))
    print(player_rhymes)

  # player has to put input into the game
    rhyme_user2 = str(input("Enter your rhyme sucker: "))

  # compare rhyme from user with syntax from bot
  def compare2(self):
    if rhyme_user2 == rhyme04:
      print("Nice try fella! ")
      print("Try again! ")
      print(str(input("Enter your rhyme sucker: ")))
    elif rhyme_user2 == rhyme05:
      print("Why are you telling the same thing, as I do? ")
      print("Try again! ")
      print(str(input("Enter your rhyme sucker: ")))
    elif rhyme_user2 == rhyme06:
      print("You beat me twice, let us see next round")

Round2 = Round2()

# Round3 battle module 
class Round3:
    def bars3(self, bar7, bar8, bar9):
      bar7 = str("Killer instinct. ")
      bar8 = str("Kill you with one ink. ")
      bar9 = str("Don't try me, otherwise you go exstinct. ")
      # mix 1st round syntax
      syntax_bot3 = [str(bar7), str(bar8), str(bar9)]
      print(syntax_bot3)

    def bars_loop2(self):
      for y in syntax_bot3:
        print(bar7)
        print(bar8)
        print(bar9)

    def options3(self, rhyme07, rhyme08, rhyme09, player_rhymes, rhyme_user3):
      rhyme07 = str("1. I am greater! ")
      rhyme08 = str("2. Kill you with one ink. ")
      rhyme09 = str("3. You fake n-sync, i terminate before an eye blink! ")
      player_rhymes = (str(rhyme07), str(rhyme08), str(rhyme09))
      print(player_rhymes)
      # player has to put input into the game
      rhyme_user3 = str(input("Enter your rhyme sucker: "))

    def compare3(self):
      for b in syntax_bot3:
        if rhyme_user3 == rhyme07:
          print("Nice try fella! ")
          print("Try again! ")
          print(str(input("Enter your rhyme sucker: ")))
        if rhyme_user3 == rhyme08:
          print("Why are you telling the same thing, as i do? ")
          print("Try again! ")
          print(str(input("Enter your rhyme sucker: ")))
        if rhyme_user3 == rhyme09:
          print("AAAAAAHHHHHH! ")
          print("You won! "+ ", " + "Let me mourn my defeat rap-samurai! ")
          break

Round3 = Round3()

# print(testing was successful!)
# for restart program use start()
# def start():
#    ...
