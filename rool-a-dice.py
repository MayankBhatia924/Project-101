import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")
    num_players = int(input("Enter the number of players: "))

    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled: {result}")

        play_again = input("Roll again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
