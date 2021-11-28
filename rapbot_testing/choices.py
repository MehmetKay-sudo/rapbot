import time
import random
import os

# BEFORE RHYME BATTLE
# building pre-requesites-----------------------------------------------------------------------------------------------
# build data for bot
bars = [str("I am here to win"), str("Not here to sing"), str("I am the king")]

# always pack bools and functions into var in order to work with them
int1 = True
int2 = False

# print rhyme choices
counter_rhymes1 = [str("You are here to sing"), str("Not here to win"), str("You are kid with no wing")]
counter_rhymes2 = [str("Never mind sucker! "), str("You will be defeated"),
                   str("This rap battle is going to be heated!"), str("An ambulance will be needed.")]
counter_rhymes3 = [str("You won.")]

# mix counter_rhymes
counter_rhymes = [counter_rhymes1, counter_rhymes2, counter_rhymes3]

# adjust counter_rhymes with booleans
counter_rhymes1 = True
counter_rhymes2 = False
counter_rhymes3 = False

# list the counter bars
print(counter_rhymes1)
print(counter_rhymes2)
print(counter_rhymes3)
# End of prerequisites--------------------------------------------------------------------------------------------------
# RHYME BATTLE BEGINS---------------------------------------------------------------------------------------------------
# establish battle statements
time.sleep(1)
print("Here are my rhymes: ")
time.sleep(1)
print(bars)
time.sleep(1)
print("Here are your choices, to rhyme against me: ")
time.sleep(1)
print(counter_rhymes)
time.sleep(2)
rhyme_user = input()
# START for loop--------------------------------------------------------------------------------------------------------
for i in bars:
    if counter_rhymes == rhyme_user:
        print("You beat me. ")
    else:
        print("You lost. ")