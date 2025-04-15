# secret word input function
from dataclasses import replace

secret_word = input("Player 1: Choose a secret word:")

# try counter
n_tries = 0

# letter input function
letter = input("Player 2: Choose a letter:")

# word status displayer
def word_status(secret_word, letter):
    for elem in secret_word.upper():
        if elem != letter:
            print("_", end=" ")
        else:
            print(letter, end=" ")

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
        global n_tries
        print(str(n_tries) + " out of 5 tries.")
    elif n_tries == 5:
        print(str(n_tries) + " out of 5 tries. You lose!")
        return False

# letter list function
def letter_list(letter):
    letter_list = []
    if letter not in letter_list:
        letter_list.append(letter)
    else:
        print(letter + "has already been chosen. Choose another letter!")
# the game
def hangman():
    n_tries = 0
    secret_word = input("Player 1: Choose a secret word:")
    try_word = set_try_word(secret_word)
    while True:
        letter = input("Player 2: Choose a letter:")
        try_word = word_status(secret_word, letter, try_word)
        failed_attempts(secret_word, letter, n_tries)

hangman()



