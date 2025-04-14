# secret word input function
secret_word = input("Player 1: Choose a secret word:")

# try counter
n_tries = 0

# letter input function
letter = input("Player 2: Choose a letter:")

# word status displayer
def word_status():
    for elem in secret_word.upper():
        if elem != letter:
            print("_", end=" ")
        else:
            print(letter, end=" ")

# failed attempts function
def failed_attempts():
    global n_tries
    if letter not in secret_word:
        n_tries += 1
        print(str(n_tries) + " out of 5 tries.")
    elif n_tries == 5:
        print(str(n_tries) + " out of 5 tries. You lose!")
        return False




