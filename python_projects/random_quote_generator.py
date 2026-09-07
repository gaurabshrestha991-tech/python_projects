# Random quote generator

import random

quotes = [
    "Believe in yourself.",
    "Never give up.",
    "Success comes from hard work.",
    "Every day is a new beginning.",
    "Dream big and work hard.",
    "Mistakes are proof that you are trying."
]

while True:
    print("\nRandom Quote Generator")
    print("------------------------")
    
    input("Press Enter to get a quote...")
    
    quote = random.choice(quotes)
    print("\n\"" + quote + "\"")
    
    choice = input("\nGet another quote? (y/n): ").lower()
    
    if choice != "y":
        print("Thnak You!")
        break
    