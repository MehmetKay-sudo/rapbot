from time import sleep
import random as rn

# this is a battle round module
# write a main function
def main():
    print(rhymegen)

# introduction
bars = [str("I am here to win"), str("Not here to sing"), str("I am the king")]

# print rhyme choices
counter_rhyme1 = "You are here to sing. " + "Not here to win. " + "You are kid with no wing. "
counter_rhyme2 = "This rap battle is going to be heated! " + "An ambulance will be needed. "

# mix counter_rhymes
counter_rhymes = (counter_rhyme1, counter_rhyme2)

# print counter rhymes for selection
print(counter_rhymes)

# generate input function
counter = input("Choose rhyme for counter attack: ")

# write generate for measuring options
def rhymegen():
    while True:
        for counter in counter_rhymes:
            if counter == counter_rhyme1:
                print("You beat me. " + "let's go to the next round. ")
            else:
                print("This is not enough sucker! " + "Try again. ")

rhymegen = rhymegen()
