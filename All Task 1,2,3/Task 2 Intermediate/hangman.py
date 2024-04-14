import random

# List of words for the game
words = ["python", "hangman", "computer", "programming", "keyboard", "algorithm", "developer", "software", "engineer"]

# Select a random word from the list
word = random.choice(words)

# Convert the word to lowercase for case-insensitive comparison
word = word.lower()

# Initialize variables
guessed_letters = []
max_attempts = 6
attempts = 0

# Print initial message
print("Welcome to Hangman!")
print("Try to guess the word.")

# Main game loop
while True:
    # Print the word with blanks for the letters not yet guessed
    progress = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("Progress:", progress)

    # Ask for user input (a letter guess or hint)
    guess = input("Enter a letter guess or 'hint' for a hint: ").lower()

    # Check if the user asked for a hint
    if guess == "hint":
        # Choose a random letter from the word that hasn't been guessed yet
        hint = random.choice([letter for letter in word if letter not in guessed_letters])
        print("Hint: The word contains the letter", hint)
        continue

    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print("Correct guess!")
    else:
        print("Incorrect guess.")
        attempts += 1

    # Check if the player has won or lost
    if "_" not in progress:
        print("Congratulations! You've guessed the word:", word)
        break
    elif attempts >= max_attempts:
        print("Sorry, you've run out of attempts. The word was:", word)
        break
