# secret word input function
secret_word = input("Player 1: Choose a secret word:")

# try counter
n_tries = 0

# letter input function
letter = input("Player 2: Choose a letter:")

# word status displayer
def word_status():
    global n_tries
    for elem in secret_word.upper():
        if elem != letter:
            print("_", end=" ")
            print(str(n_tries) + "out of 5 tries.")
            n_tries += 1

        else:
            print(letter, end=" ")

word_status()



