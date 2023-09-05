import time

def main():
    battle = RapBattle()

    intro = battle.intro
    simulation1 = battle.simulation1
    simulation2 = battle.simulation2
    simulation3 = battle.simulation3
    bars = battle.bars
    bars2 = battle.bars2
    bars3 = battle.bars3
    options = battle.options
    option2 = battle.options2
    options3 = battle.options3
    compare = battle.compare
    compare2 = battle.compare2
    compare3 = battle.compare3
    bars_loop = None  # Add definitions for bars_loop and bars_loop2
    bars_loop2 = None

    intro()
    simulation1()
    simulation2()
    simulation3()
    bars("I rhyme fine!", "I rhyme great!", "I am the best in the state!")
    options("1. I am greater!", "2. I rhyme great!", "3. You ain't a saint, the worst in the state!")
    compare("1. I am greater!", "2. I rhyme great!", "3. You ain't a saint, the worst in the state!")
    bars2("I am straight!", "Big my brain!", "Skilled and insane!")

if __name__ == "__main__":
    main()

class RapBattle:
    def __init__(self):
        self.name = ["cherry", "fearless", "rose"]
        self.player_name = ""
        self.rhyme_user = ""

    def intro(self):
        print(self.name)
        select = input("Enter your name: ")
        if select in self.name:
            print("Battlename successfully selected")
        else:
            print("Invalid name. Try again.")

    def simulation1(self):
        def intro():
            if self.player_name in self.name:
                time.sleep(1)
                dot = "."
                print(dot * 3 + "processing data" + dot * 3)
                time.sleep(2)
                print("Please wait.")
                time.sleep(3)
                print("Name chosen.")
                time.sleep(1)

        intro()

    def simulation2(self):
        print("You wanna rhyme against me? ")
        print("Let's see what you got!")
        time.sleep(2)
        print("Are you READY? ")
        time.sleep(1)

    def simulation3(self):
        time.sleep(2)
        print("Let's go in..." + "3" + "...")
        time.sleep(1)
        print("Let's go in..." + "2" + "...")
        time.sleep(1)
        print("Let's go in..." + "1" + "...")
        time.sleep(1)

    def bars(self, bar1, bar2, bar3):
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
                break

    def options(self, rhyme01, rhyme02, rhyme03):
        rhyme01 = str("1. I am greater! ")
        rhyme02 = str("2. I rhyme great! ")
        rhyme03 = str("3. You ain't a saint, the worst in the state!")
        player_rhymes = (str(rhyme01), str(rhyme02), str(rhyme03))
        print(player_rhymes)
        # player has to put input into the game
        time.sleep(1)
        self.rhyme_user = input("Enter your rhyme sucker: ")

    def compare(self, rhyme01, rhyme02, rhyme03):
        syntax_bot = [rhyme01, rhyme02, rhyme03]
        for z in syntax_bot:
            if self.rhyme_user == z:
                if self.rhyme_user == rhyme01:
                    print("Nice try fella! ")
                    print("Try again! ")
                    self.rhyme_user = input("Enter your rhyme sucker: ")
                elif self.rhyme_user == rhyme02:
                    print("Why are you telling the same thing as I do? ")
                    print("Try again! ")
                    self.rhyme_user = input("Enter your rhyme sucker: ")
                elif self.rhyme_user == rhyme03:
                    print("AAAAAAHHHHHH! ")
                    print("You beat me once, Let's see what you will do in the next round! ")
                    break

    # Define the remaining methods for Round2 and Round3 in a similar way
