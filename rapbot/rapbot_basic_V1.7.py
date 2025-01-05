import time

# Define the main RapBattle class to handle game flow and interactions.
class RapBattle:
    def __init__(self):
        self.bot_name = "Rapbot"
        self.name_select = ["cherry", "fearless", "killer", "savage", "beast", "king", "queen", "god", "devil", "angel", "demon", "saint", "sin"]
        self.user_name = ""

    # Start the intro for the rap bot.
    def intro(self):
        print("Welcome to the Rap Battle!")
        print("Choose a battlename from the following options:")
        print(self.name_select)

        while True:
            self.user_name = input("Enter your name: ")
            if self.user_name in self.name_select:
                print("Battlename successfully selected!")
                break
            else:
                print("Invalid name. Try again.")

    # Simulate battle phases with countdowns.
    def start_battle(self):
        print(f"{self.user_name}, you dare challenge {self.bot_name}?")
        time.sleep(1)
        print("Let's go in... 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        print("Battle Begins!")
        time.sleep(1)

# Define the Round class to manage the structure of each battle round.
class Round:
    def __init__(self, bars, rhymes):
        self.bars = bars
        self.rhymes = rhymes

    # Print the bot's bars (lines) for the round.
    def display_bars(self):
        print("Rapbot spits:")
        for bar in self.bars:
            print(bar)
        time.sleep(1)

    # Show player's rhyme options and get input
    def player_turn(self):
        print("\nYour choices:")
        for i, rhyme in enumerate(self.rhymes, start=1):
            print(f"{i}. {rhyme}")
        while True:
            try:
                choice = int(input("Choose your rhyme by entering the number: "))
                if 1 <= choice <= len(self.rhymes):
                    return self.rhymes[choice - 1]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")

    # Compare the player's rhyme to determine if they beat the bot's rhymes.
    def compare_rhyme(self, user_rhyme):
        bot_rhyme = self.rhymes[-1]  # The third rhyme is always the winning response
        if user_rhyme == bot_rhyme:
            print("You won this round!")
            return True
        elif user_rhyme == self.rhymes[1]:
            print("Why are you saying the same thing as me? Try again!")
            return False
        else:
            print("Nice try, but that's not good enough! Try again!")
            return False

# Define the game loop and rounds in the main function.
def main():
    # Initialize the Rap Battle
    battle = RapBattle()
    battle.intro()
    battle.start_battle()

    # Define the rounds
    rounds = [
        Round(
            bars=["I rhyme fine!", "I rhyme great!", "I am the best in the state!"],
            rhymes=["I am greater!", "I rhyme great!", "You ain't a saint, the worst in the state!"]
        ),
        Round(
            bars=["I am straight!", "Big my brain!", "Skilled and insane!"],
            rhymes=["You are late!", "Big my brain!", "You just faint and I maintain!"]
        ),
        Round(
            bars=["Killer instinct.", "Kill you with one ink.", "Don't try me, otherwise you go extinct."],
            rhymes=["I am greater!", "Kill you with one ink.", "You fake n-sync, I terminate before an eye blink!"]
        ),
    ]

    # Play each round
    for round_num, round_obj in enumerate(rounds, start=1):
        print(f"\nRound {round_num}:")
        round_obj.display_bars()
        while True:
            user_rhyme = round_obj.player_turn()
            if round_obj.compare_rhyme(user_rhyme):
                break

    print("\nCongratulations! You've beaten Rapbot!")

# Run the main function to start the game
if __name__ == "__main__":
    main()
