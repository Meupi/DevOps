# secret word input function
secret_word = input("Player 1: Choose a secret word:")

# letter input function
letter = input("Player 2: Choose a letter:")

# word status displayer
def word_status():
    for elem in secret_word.upper():
        if elem != letter:
            print("_", end=" ")
        else:
            print(letter, end=" ")

word_status()



