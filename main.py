import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == '__main__':
    print("Welcome to the dice rolling simulator!")
    while True:
        roll = roll_dice()
        print(f"You rolled a {roll}")
        response = input("Would you like to roll again? (yes/no)")
        if response.lower() != 'yes':
            break
    print("Thanks for playing!")
