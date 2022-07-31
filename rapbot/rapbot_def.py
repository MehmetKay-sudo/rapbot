
# write a main function
def main():
    print(bars)
    print(bars2)
    print(bars3)

# create a bar_generator / specific
def bars():
    bar1 = str("I rhyme fine!")
    bar2 = str("I rhyme great!")
    bar3 = str("I am the best in the state!")

bars = bars()

def bars2():
    bar4 = str("I am straight! ")
    bar5 = str("Big my brain! ")
    bar6 = str("Skilled and insane! ")

bars2 = bars()

def bars3():
    bar7 = str("Killer instinct. ")
    bar8 = str("Kill you with one ink. ")
    bar9 = str("Don't try me, otherwise you go exstinct. ")

bars3 = bars3()

bars = (bars, bars2, bars3)
print(bars)
