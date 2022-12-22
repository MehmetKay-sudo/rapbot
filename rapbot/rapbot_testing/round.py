# 2ND ROUND OF BATTLE---------------------------------------------------------------------------------------------------
# creating second syntax
pronouns2 = (str("he"), str("she"), str("it"), str("they"))
verbs2 = (str("think"), str("drink"), str("blink"))
adjectives2 = (str("great"), str("greedy"), str("fast"))

syntax_bot2 = [pronouns2, verbs2, adjectives2]

# creating loop2 for syntax02
for i in syntax_bot2:
    if i in syntax_bot2:
        print(pronouns2[0:1])
        print(verbs2[0:1])
        print(adjectives2[0:1])
    break

# player has to put input into the game
rhyme_user = str(input("Enter your rhyme sucker: "))

# compare rhyme from user with syntax from bot
for i in syntax_bot2:
    if rhyme_user == "he is dumb ":
        print("Nice try fella! ")
        time.sleep(1)
        print("Try again! ")
    print(rhyme_user)

    if rhyme_user == "he thinks great ":
        print("Why are you telling the same thing, as i do? ")
        time.sleep(1)
        print("Try again! ")
    print(rhyme_user)

    if rhyme_user == "he tries to be smart! ":
        print("You beat me once, let us see next round")
    break

# does not work as expected