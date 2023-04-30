import random
# second words is the variable
from words import words


def get_valid_word(words):
    word = random.choice(words)

    while "-" or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman(words):
    word = get_valid_words(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    