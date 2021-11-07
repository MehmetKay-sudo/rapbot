import random

# battle starts
print("You wanna rhyme against me? " + "Let's see, what you got!")
print("Are you ready?")

# building syntax
pronouns = (str("he"), str("she"), str("it"))
verbs = (str("does"), str("rhymes"), str("lies"))
adjectives = (str("big"), str("small"), str("tough"))

syntax01 = [pronouns, verbs, adjectives]

# creating loops for Syntax01
for i in syntax01:
    if i in syntax01:
        print(pronouns[0:1])
        print(verbs[0:1])
        print(adjectives[0:1])
    break

# separate the rhyme
print(", ")

# creating second syntax
pronouns2 = (str("he"), str("she"), str("it"), str("they"))
verbs2 = (str("think"), str("drink"), str("blink"))
adjectives2 = (str("great"), str("greedy"), str("fast"))

syntax02 = [pronouns2, verbs2, adjectives2]

# creating loop2 for syntax02
for i in syntax02:
    if i in syntax02:
        print(pronouns2[0:1])
        print(verbs2[0:1])
        print(adjectives2[0:1])
    break

# aim for the next session
# create an input function call, through which the player can interact with the bot
# 1st option: player presses one word into the call and bot gives a word back
# 2nd option: bot rhymes one rhyme and the player has to complete the rhyme line
# next step is to modify code in def functions / f.e. def syntax01 (): ...
# how can i merge the rhyme lines into one rhyme line again
