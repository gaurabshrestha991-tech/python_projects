#   Dice Rolling Simulator

import random

while True:
    print("\nDice Rolling Simulator")
    print("------------------------")
    
    input("Press Enter to roll the dice")
    
    dice = random.randint(1, 6)
    print("You rolled:", dice)
    
    choice = input("\nRoll again? (y/n): ").lower()
    
    if choice != "y":
        print("Thanks for playing!")
        break