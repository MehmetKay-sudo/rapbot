import os
import json
import time
import random

# =============================================================================
# 1. OpenCode Go API Connection Setup
# =============================================================================
from openai import OpenAI

def _load_opencode_key():
    key = os.environ.get("OPENCODE_ZEN_API_KEY")
    if key:
        return key
    auth_path = os.path.expanduser("~/.local/share/opencode/auth.json")
    try:
        with open(auth_path) as f:
            return json.load(f)["opencode-go"]["key"]
    except Exception:
        pass
    return None

API_KEY = _load_opencode_key()
client = OpenAI(
    api_key=API_KEY,
    base_url="https://opencode.ai/zen/go/v1",
)
MODEL = "deepseek-v4-flash"

def get_chatgpt_response(prompt):
    """
    Sends a prompt to OpenCode Go (deepseek-v4-flash)
    and returns the result. Includes basic error handling.
    """
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a creative rap battle assistant. Your responses should be short, punchy, and rhyme well."},
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=300,
            temperature=0.9
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        msg = str(e)
        if "401" in msg or "403" in msg or "auth" in msg.lower():
            return "Error: API key is invalid or missing. Set OPENCODE_ZEN_API_KEY."
        return f"Error: {msg}"

# =============================================================================
# 2. Rap Battle Game Classes
# =============================================================================

class RapBattle:
    NAME_OPTIONS = [
        "cherry", "fearless", "killer", "savage", "beast",
        "king", "queen", "god", "devil", "angel", "demon", "saint", "sin"
    ]

    def __init__(self, bot_name="Rapbot"):
        self.bot_name = bot_name
        self.user_name = None
        self.memory_texts = []

    def load_memory(self, folder="memory"):
        if not os.path.exists(folder):
            print(f"No memory folder '{folder}' found. Create one with .txt files for better rap generation.")
            return

        files = [f for f in os.listdir(folder) if f.endswith(".txt")]
        if not files:
            print(f"No text files found in '{folder}'. Rapbot's vocabulary might be limited.")
            return

        for filename in files:
            file_path = os.path.join(folder, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.memory_texts.append(content)
                    print(f"Loaded memory file: {filename}")
            except Exception as e:
                print(f"Error loading {filename}: {e}")

        print(f"Loaded {len(self.memory_texts)} memory files.")
        if not self.memory_texts:
            print("Warning: No memory texts loaded. Rapbot will rely solely on its default LLM knowledge.")

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

        print(f"\n{self.user_name}, you dare challenge {self.bot_name}?")
        for count in range(3, 0, -1):
            print(f"{count}...")
            time.sleep(1)
        print("Battle begins!")
        time.sleep(1)


class Round:
    def __init__(self, battle_instance):
        self.battle = battle_instance
        self.bot_bars = []
        self.player_choices = []
        self.winning_rhyme = ""

    def generate_bot_rap(self, previous_line=""):
        context = " ".join(self.battle.memory_texts[-min(len(self.battle.memory_texts), 3):])
        if previous_line:
            prompt = (f"As a skilled rapper, spit a 2-line diss verse that rhymes with and tops this: '{previous_line}'. "
                      f"Consider these themes/words if possible: {context}. Be aggressive and confident.")
        else:
            prompt = (f"As a skilled rapper named {self.battle.bot_name}, spit an aggressive 2-line opening diss verse against {self.battle.user_name}. "
                      f"Consider these themes/words if possible: {context}. Make it punchy and rhyme.")

        print(f"\n{self.battle.bot_name} is thinking...")
        bot_response = get_chatgpt_response(prompt)
        lines = [line.strip() for line in bot_response.split('\n') if line.strip()]
        if len(lines) >= 2:
            self.bot_bars = lines[:2]
        elif lines:
            self.bot_bars = [lines[0], ""]
        else:
            self.bot_bars = ["Yo, I'm ready to flow!", "My rhymes are gonna blow!"]

        if "Error:" in self.bot_bars[0]:
            print(self.bot_bars[0])
            self.bot_bars = ["My systems are down!", "But I still wear the crown!"]
            time.sleep(2)

    def display_bars(self):
        print(f"\n{self.battle.bot_name} spits:")
        for bar in self.bot_bars:
            print(bar)
        time.sleep(1)

    def generate_player_choices(self):
        last_bot_line = self.bot_bars[-1] if self.bot_bars else "My mic is ready to ignite!"

        winning_prompt = (f"As {self.battle.user_name}, give a single, strong, rhyming counter-line "
                          f"to this: '{last_bot_line}'. Make it truly beat the opponent. Just the line.")
        self.winning_rhyme = get_chatgpt_response(winning_prompt)
        if "Error:" in self.winning_rhyme:
            print(self.winning_rhyme)
            self.winning_rhyme = f"I'm too good, can't be beat! (Error fallback for: {last_bot_line})"

        filler_rhymes = []
        for _ in range(2):
            filler_prompt = (f"Give a single, rhyming line to this: '{last_bot_line}', "
                             f"but make it sound a bit weak or generic. Just the line.")
            filler_rhyme = get_chatgpt_response(filler_prompt)
            if "Error:" in filler_rhyme:
                filler_rhyme = f"That's all you got? (Error fallback for: {last_bot_line})"
            filler_rhymes.append(filler_rhyme)

        self.player_choices = [self.winning_rhyme] + filler_rhymes
        random.shuffle(self.player_choices)

    def player_turn(self):
        print("\nYour choices:")
        for idx, rhyme in enumerate(self.player_choices, start=1):
            print(f"{idx}. {rhyme}")

        while True:
            try:
                choice = int(input(f"Choose your rhyme, {self.battle.user_name}, by entering the number: "))
                if 1 <= choice <= len(self.player_choices):
                    return self.player_choices[choice - 1]
                print("Choice number out of range. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def compare_rhyme(self, user_rhyme):
        if user_rhyme == self.winning_rhyme:
            print("\n🔥 BOOM! You nailed it! That rhyme was fire! 🔥")
            return True
        else:
            print("\n🙅‍♂️ Nah, that ain't it. Rapbot's still standing strong! Try again! 🙅‍♂️")
            return False


# =============================================================================
# 3. Game Loop with Relaunch Feature
# =============================================================================

def battle_game():
    battle = RapBattle()
    battle.load_memory()
    battle.choose_battlename()
    battle.start_battle()

    num_rounds = 3
    player_wins = 0
    bot_wins = 0

    for round_num in range(1, num_rounds + 1):
        print(f"\n--- Round {round_num} ---")
        current_round = Round(battle)

        if round_num == 1:
            current_round.generate_bot_rap()
        else:
            current_round.generate_bot_rap(
                previous_line=current_round.bot_bars[-1] if current_round.bot_bars else ""
            )
        current_round.display_bars()

        round_won = False
        attempts = 2
        while not round_won and attempts > 0:
            current_round.generate_player_choices()
            user_rhyme = current_round.player_turn()
            if current_round.compare_rhyme(user_rhyme):
                player_wins += 1
                round_won = True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"You have {attempts} attempt(s) left for this round.")
                else:
                    print("Out of attempts! Rapbot takes this round!")
                    bot_wins += 1

        time.sleep(1)

    print("\n--- Battle Results ---")
    print(f"{battle.user_name}: {player_wins} rounds won")
    print(f"{battle.bot_name}: {bot_wins} rounds won")

    if player_wins > bot_wins:
        print("\n👑 YOU ARE THE RAP KING/QUEEN! CONGRATULATIONS! 👑")
        final_rap_prompt = (f"Write a short, triumphant rap verse for {battle.user_name} celebrating their victory over Rapbot. "
                            f"Mention their skill and the defeat of the bot.")
    elif bot_wins > player_wins:
        print("\n💀 RAPBOT DOMINATES! You've been out-rhymed! Better luck next time! 💀")
        final_rap_prompt = (f"Write a short, boastful rap verse from Rapbot celebrating its victory over {battle.user_name}. "
                            f"Mention its superior skill and the opponent's defeat.")
    else:
        print("\n🤝 IT'S A TIE! A true clash of titans! 🤝")
        final_rap_prompt = (f"Write a short rap verse about an epic rap battle ending in a tie between {battle.user_name} and Rapbot. "
                            f"Mention the skill on both sides.")

    print("\nOpenCode's Final Verdict Rap:")
    final_rap_response = get_chatgpt_response(final_rap_prompt)
    print(final_rap_response)


def main():
    while True:
        battle_game()
        replay = input("\nDo you want to battle again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for battling! Peace out! 🎤")
            break
        else:
            print("\nRestarting the mic drop... 🎤\n")
            time.sleep(2)


if __name__ == "__main__":
    main()
