import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)     #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    #user typed letters
    lives = 6

    #getting user inputs
    while len(word_letters)>0 and lives>0:
        print('Lives remining: ', lives ,'and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    #gets here when len(word_letters)=0
    if lives == 0:
        print("\nYou died, correct word is " + word)
    else:
        print("\nYayy, You have guess the word " + word)


hangman()