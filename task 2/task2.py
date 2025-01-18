import random

def choose_word():
    words = ['python', 'java', 'hangman', 'computer', 'programming', 'developer', 'algorithm']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit for incorrect guesses
    guessed_word = display_word(word, guessed_letters)

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while incorrect_guesses < max_incorrect_guesses and '_' in guessed_word:
        print(f"Word: {guessed_word}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        guessed_word = display_word(word, guessed_letters)

    if '_' not in guessed_word:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"You've lost! The word was: {word}")

if __name__ == "__main__":
    hangman()
