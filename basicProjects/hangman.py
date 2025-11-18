import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have used these letters: ", ' '.join(sorted(used_letters)))
        print(f"You have {lives} lives left.")

        # Show the current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")
            else:
                lives -= 1
                print("Letter not in word.")
                print(f"You have {lives} lives left.")

        elif user_letter in used_letters:
            print("You already used that letter.")
        else:
            print("Invalid input. Use letters A–Z.")
    # WIN or LOSE
    if lives == 0:
        print(f"\n💀 You lost! The word was: {word}")
    else:
        print(f"\n🎉 You guessed the word! It was: {word}")

hangman()
