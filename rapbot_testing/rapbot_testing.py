import random

# battle starts
print("You wanna rhyme against me?" + "Let's see, what you got!")

# building syntax
pronouns = (str("he"), str("she"), str("it"))
verbs = (str("does"), str("rhymes"), str("lies"))
adjectives = (str("big"), str("small"), str("tough"))

syntax01 = [pronouns, verbs, adjectives]

# creating loops for every syntax-complex
for i in syntax01:
    if i in syntax01:
        print("This is the 1st round!")


