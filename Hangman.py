# secret word input function
from dataclasses import replace

secret_word = input("Player 1: Choose a secret word:")

# try counter
n_tries = 0

# letter input function
letter = input("Player 2: Choose a letter:")

# word status displayer
def word_status(secret_word, letter, try_word):
    position = [index for index,char in enumerate(secret_word) if char == letter]
    try_word_ls = list(try_word)
    for index in position:
        try_word_ls[index] = secret_word[index]
    try_word = "".join(try_word_ls)
    print(try_word)
    return try_word

# try_word funtion
def set_try_word(secret_word):
    try_word_ls = []
    for comp in range(len(secret_word)):
        try_word_ls.append("_")
    try_word = "".join(try_word_ls)
    return try_word

# failed attempts function
def failed_attempts(secret_word, letter, n_tries):
    if letter not in secret_word:
        n_tries += 1
        print(str(n_tries) + " out of 5 tries.")
        return n_tries


def loop_breaker(secret_word, try_word, n_tries):
    if secret_word != try_word and n_tries != 5:
        return True
    elif secret_word == secret_word:
        return False
    else:
        return False

# letter list function
def letter_list(letter):
    if letter not in letter_list:
        letter_list.append(letter)
    else:
        print(letter + "has already been chosen. Choose another letter!")

def outcome(n_tries, secret_word, try_word):
    if n_tries == 5 and secret_word != try_word:
        print("You loose!")
    elif secret_word == try_word:
        print("Congrats! You won!")

# the game
def hangman():
    n_tries = 0
    letter_list = []
    secret_word = input("Player 1: Choose a secret word:")
    try_word = set_try_word(secret_word)
    while loop_breaker(secret_word, try_word, n_tries):
        letter = input("Player 2: Choose a letter:")
        try_word = word_status(secret_word, letter, try_word)
        n_tries = failed_attempts(secret_word, letter, n_tries)
    outcome(n_tries, secret_word, try_word)
hangman()
