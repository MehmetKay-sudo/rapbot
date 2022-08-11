# beginning was optimized by co-programmer

from os import system
from time import sleep

# init all phrases
PHRASES: dict = {
    'names': ['cherry', 'fearless', 'rose'],
    'choosing_sequence': 'Choose your name: ',
    'starting_sequence': [
        f'{10*"."}processing data{10*"."}', 'Please wait.', 'Name chosen.',
        'You wanna rhyme against me?', "Let's see, what you got!",
        'Are ', 'you ', 'READY?',
    ] + [f"Let's go in ... {i} ... " for i in range(1, 4)]
}


def start_rap_battle() -> None:
    name: str = str(input(f'{" ".join(PHRASES["names"])} \n {PHRASES["choosing_sequence"]}')).strip().lower()

    if name in PHRASES["names"]:
        for pharse in PHRASES['starting_sequence']:
            sleep(1)
            system('clear')
            print(pharse)


if __name__ == '__main__':
    start_rap_battle()


