from time import sleep
import random as rn

# this is a battle round module
# write a main function
def main():
    print(bot_bars)
    print(counter_rhymes)
    print(rhymegen)

# introduction
def bars():
    bot_bars1 = "I am the rapbot. " + "call me the rapgod. "
    bot_bars2 = "Try to beat me. " + "This will not be easy. "

bot_bars = bars()

# print rhyme choices
def counter_rhymes():
    counter_rhymes1 = "1" + ": " + "You are here to sing. " + "Not here to win. " + "You are kid with no wing. "
    counter_rhymes2 = "2" + ": " + "This rap battle is going to be heated! " + "An ambulance will be needed. "

counter_rhymes = counter_rhymes()

# generate input function
counter = input("Choose rhyme for counter attack through pressing 1 and 2: ")

# write generate for measuring options
def rhymegen():
    while True:
        for counter in counter_rhymes:
            if counter == counter_rhyme1:
                print("You beat me. " + "let's go to the next round. ")
            else:
                print("This is not enough sucker! " + "Try again. ")

rhymegen = rhymegen()
