import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    wordLetters = set(word)
    alphabets = set(string.ascii_uppercase)
    
    used_letters = set()
    lives = 6

    while len(wordLetters) > 0 and lives >0:
        print('Remaining lives: ', lives ,' and the used letters are: ', ' '.join(used_letters))        
        wordList = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(wordList))
        user_letter = input("Guess a word: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in wordLetters:
                wordLetters.remove(user_letter)
            else:
                lives -=1
        elif user_letter in used_letters:
            print("This character is already used. Please try again.")
        else:
            print("Invalid characters")
    if lives == 0:
        print("\n\nYou died, the word is", word ,"\n")
    else:
        print("\n\nYayy!! you have guessed the word. " + word + "\n")
    

hangman()
