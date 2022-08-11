from time import sleep
import random as rn

# this is a battle round module
# write a main function
#def main():
#    print(bot_bars)
#    print(counter_rhymes)
#    print(rhymegen)

# introduction
def bars(x, y):
    return x+y
    import time
    x = "I am the rapbot. " + "call me the rapgod. "
    time.sleep(1)
    y = "Try to beat me. " + "This will not be easy. "

# print rhyme choices
def counter_rhymes(g, h):
    return g+h
    g = "1" + ": " + "You are here to sing. " + "Not here to win. " + "You are kid with no wing. "
    h = "2" + ": " + "This rap battle is going to be heated! " + "An ambulance will be needed. "

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
