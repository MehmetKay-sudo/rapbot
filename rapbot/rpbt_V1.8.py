import time
import sys, os
import openai

# =============================================================================
# 1. ChatGPT API Connection Setup
# =============================================================================
# Replace "YOUR_API_KEY_HERE" with your actual API key.
openai.api_key = "YOUR_API_KEY_HERE"

def get_chatgpt_response(prompt):
    """
    Sends a prompt to the ChatGPT API (using model gpt-3.5-turbo)
    and returns the result.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative rap battle assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# =============================================================================
# 2. Rap Battle Game Classes
# =============================================================================

class RapBattle:
    def __init__(self):
        self.bot_name = "Rapbot"
        self.name_select = ["cherry", "fearless", "killer", "savage", "beast", 
                            "king", "queen", "god", "devil", "angel", "demon", 
                            "saint", "sin"]
        self.user_name = ""

    def intro(self):
        print("Welcome to the Rap Battle!")
        print("Choose a battlename from the following options:")
        print(self.name_select)
        while True:
            self.user_name = input("Enter your battlename: ")
            if self.user_name in self.name_select:
                print("Battlename successfully selected!")
                break
            else:
                print("Invalid battlename. Try again!")

    def start_battle(self):
        print(f"\n{self.user_name}, you dare challenge {self.bot_name}?")
        # Countdown before the battle begins.
        for count in range(3, 0, -1):
            print(f"Let's go in... {count}...")
            time.sleep(1)
        print("Battle Begins!")
        time.sleep(1)

class Round:
    def __init__(self, bars, rhymes):
        self.bars = bars
        self.rhymes = rhymes

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
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    def compare_rhyme(self, user_rhyme):
        # Here the winning rhyme is always the last one in the list.
        winning_rhyme = self.rhymes[-1]
        if user_rhyme == winning_rhyme:
            print("You won this round!")
            return True
        elif user_rhyme == self.rhymes[1]:
            print("Why are you saying the same thing as me? Try again!")
            return False
        else:
            print("Nice try, but that's not good enough! Try again!")
            return False

# =============================================================================
# 3. Game Loop with Relaunch Feature
# =============================================================================

def battle_game():
    # Initialize the battle game.
    battle = RapBattle()
    battle.intro()
    battle.start_battle()

    # Define the rounds.
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

    # Execute each round.
    for round_num, round_obj in enumerate(rounds, start=1):
        print(f"\n--- Round {round_num} ---")
        round_obj.display_bars()
        while True:
            user_rhyme = round_obj.player_turn()
            if round_obj.compare_rhyme(user_rhyme):
                break

    print("\nCongratulations! You've beaten Rapbot!")
    
    # -----------------------------------------------------------------------------
    # 4. Get a Congratulatory Rap from ChatGPT
    # -----------------------------------------------------------------------------
    prompt = (f"Write a short congratulatory rap verse for {battle.user_name}, "
              "who just defeated Rapbot in an epic rap battle.")
    chatgpt_rap = get_chatgpt_response(prompt)
    print("\nChatGPT's Congratulatory Rap:")
    print(chatgpt_rap)

def main():
    while True:
        battle_game()
        # Ask if the user wants to play another round.
        replay = input("\nDo you want to play again? (y/n): ")
        if replay.lower() != "y":
            print("Goodbye!")
            break
        else:
            print("\nRestarting the game...\n")
            time.sleep(1)
            # Optionally, you could also clear the terminal screen here.

if __name__ == "__main__":
    main()
