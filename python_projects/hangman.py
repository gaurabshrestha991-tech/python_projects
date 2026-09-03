import random

words = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "internet",
    "github",
    "software"
]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to HANGMAN")

display = ["_"] * len(word)

while wrong_guesses < max_attempts and "_" in display:
    print("\nWord", "".join(display))
    print("Guessed letters:", "".join(guessed_letters))
    print("Attempts left: ", max_attempts - wrong_guesses)
    
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    
    if guess in word:
        print("Correct guess!")
        
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
                
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        
print("\n-----------------------")

if "_" not in display:
    print("Congratulation! You won!")
    print("The word was: ", word)
    
else:
    print("Game Over!")
    print("The word was:", word)
    
print("-------------------------------------")