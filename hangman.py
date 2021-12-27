import random
from words import words
import string
# print(words)

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list (words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

# getting user inmput
    while len(word_letters) > 0 and lives > 0:
# letters used
# ' '.join(['a', 'b', 'cd'])-->'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        # what currect word is with dashes in place of missing letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 #takes away a life if wrong letter is slected

        elif user_letter in used_letters:
            print('You have already used that character. Please Try a different letter.')
        else:
            print('Invalid character. Please try again.')

            # gets here when len(word_letters) == 0 which means when they either win or they run out of lives you exit the loop.
    if lives == 0:
        print('Sorry You have died playing Hangman The Word was', word)
    else:
        print('You have successfully guessed the word', word, '!! Great Job!')
hangman()
# user_input = input('Type Something Here:')
# print(user_input)