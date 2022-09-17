import random
from hangman_words import word_list
from hangman_ascii import logo, stages

print(logo)
guess_word = random.choice(word_list)

# Max try to guess the word (word length)
max_try = 6
guess = []
word_len = len(guess_word)

for pos in range(word_len):
    guess.append("_")
print(guess)

while max_try:
    letter = str(input("Please guess the letter:")).lower()

    for position in range(len(guess_word)):
        if letter == guess_word[position]:
            guess[position] = letter

    print(guess, end="")
    max_try -= 1
    print("\n")
    if '_' not in guess:
        print("Well Done!!")
        break
    if max_try == 0:
        print(f'Good Luck! Try Again. The word was {guess_word}')
        break


stages = []