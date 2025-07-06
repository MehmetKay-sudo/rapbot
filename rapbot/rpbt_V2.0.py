import os
import time
import random # Added for random rhyme selection

class RapBattle:
    # These are the acceptable battlenames
    NAME_OPTIONS = [
        "cherry", "fearless", "killer", "savage", "beast",
        "king", "queen", "god", "devil", "angel", "demon", "saint", "sin"
    ]

    def __init__(self, bot_name="Rapbot"):
        self.bot_name = bot_name
        self.api_key = None
        self.memory_texts = []
        self.user_name = None

    def set_api_key(self, api_key: str):
        self.api_key = api_key
        print("API key set successfully.")

    def load_memory(self, folder="memory"):
        if not os.path.exists(folder):
            print(f"No memory folder '{folder}' found.")
            return

        files = [f for f in os.listdir(folder) if f.endswith(".txt")]
        for filename in files:
            with open(os.path.join(folder, filename), "r", encoding="utf-8") as file:
                content = file.read()
                self.memory_texts.append(content)
                print(f"Loaded memory file: {filename}")

        if self.memory_texts:
            print(f"Loaded {len(self.memory_texts)} memory files.")
        else:
            print("No text files found in memory folder.")

    def choose_battlename(self):
        print("Welcome to the Rap Battle!")
        print("Choose your battlename from the following options:")
        print(self.NAME_OPTIONS)

        while True:
            user_input = input("Enter your chosen battlename: ").lower()
            if user_input in self.NAME_OPTIONS:
                self.user_name = user_input
                print("Battlename selected!")
                break
            else:
                print("Invalid name. Please try again.")

    def start_battle(self):
        if not self.user_name:
            print("You must select a battlename first!")
            return

        print(f"{self.user_name}, you dare challenge {self.bot_name}?")
        for count in range(3, 0, -1):
            print(f"{count}...")
            time.sleep(1)
        print("Battle begins!")
        time.sleep(1)


class Round:
    def __init__(self, bars, rhymes):
        self.bars = bars
        self.rhymes = rhymes
        # Randomly select a winning rhyme for this round to break patterns
        self.winning_rhyme = random.choice(self.rhymes)

    def display_bars(self):
        print("\nRapbot spits:")
        for bar in self.bars:
            print(bar)
        time.sleep(1)

    def player_turn(self):
        print("\nYour choices:")
        for idx, rhyme in enumerate(self.rhymes, start=1):
            print(f"{idx}. {rhyme}")

        while True:
            try:
                choice = int(input("Choose your rhyme by entering the number: "))
                if 1 <= choice <= len(self.rhymes):
                    return self.rhymes[choice - 1]
                print("Choice number out of range. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def compare_rhyme(self, user_rhyme):
        # Now compares against the randomly chosen winning_rhyme
        if user_rhyme == self.winning_rhyme:
            print("You won this round!")
            return True
        elif user_rhyme == self.rhymes[1] and user_rhyme != self.winning_rhyme: # Still gives a specific message if repeating bot's, but only if it's not the winning rhyme
            print("You're just repeating the bot's rhyme. Try another line!")
        else:
            print("Nice try, but that's not quite right. Try again!")
        return False


def main():
    battle = RapBattle()
    # Note: API key is set, but not actively used for dynamic generation in this version
    battle.set_api_key("your-api-key-here")
    battle.load_memory() # Loads memory texts, but current version doesn't use them for dynamic rhyming
    battle.choose_battlename()
    battle.start_battle()

    rounds = [
        Round(
            bars=["I rhyme fine!", "I rhyme great!", "I'm the best in the state!"],
            rhymes=["I am greater!", "I rhyme great!", "You ain't a saint, worst in the state!"]
        ),
        Round(
            bars=["I am straight!", "Big my brain!", "Skilled and insane!"],
            rhymes=["You're running late!", "Big my brain!", "I maintain while others faint!"]
        ),
        Round(
            bars=["Killer instinct.", "Kill with one ink.", "Don't test me or go extinct."],
            rhymes=["I am greater!", "Kill with one ink.", "You fake n-sync, I terminate in a blink!"]
        ),
    ]

    for idx, round_obj in enumerate(rounds, start=1):
        print(f"\n--- Round {idx} ---")
        while True: # Loop for the current round
            round_obj.display_bars() # Rapbot spits its bars at the start of each attempt
            user_rhyme = round_obj.player_turn()
            if round_obj.compare_rhyme(user_rhyme):
                break # Only break out of the round loop if the user wins

    print("\nCongratulations! You've beaten Rapbot!")


if __name__ == "__main__":
    main()
