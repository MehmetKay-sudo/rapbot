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
    import time
    x = "I am the rapbot. " + "call me the rapgod. "
    time.sleep(1)
    y = "Try to beat me. " + "This will not be easy. "
    print(x)
    print(y)
    bars = bars(x,y)
print(bars)

bars = bars()

# print rhyme choices
def counter_rhymes(g, h):
    g = "1" + ": " + "You are here to sing. " + "Not here to win. " + "You are kid with no wing. "
    h = "2" + ": " + "This rap battle is going to be heated! " + "An ambulance will be needed. "
    print(g)
    print(h)
    counter_rhymes = counter_rhymes(g,h)
print(counter_rhymes)

counter_rhymes = counter_rhymes()

# generate input function
counter = input("Choose rhyme for counter attack through pressing 1 and 2: ")

# write generate for measuring options
while True:
    if counter == counter_rhymes:
        print("You beat me. " + "let's go to the next round. ")
    else:
        print("This is not enough sucker! " + "Try again. ")
        break

# functions output:
# <function bars at 0x7f3d0f2c90d0>
# <function counter_rhymes at 0x7f3d0f04bdc0>
