import random
from Dictionary import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' 'in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    old_letters = set() # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letter) > 0 and lives > 0:
        # letters used 
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(old_letters))

        # What current word is (W - R D)
        word_list = [letter if letter in old_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        
        guessed_letter = input('Guess a letter: ').upper()
        if guessed_letter in alphabet - old_letters:
            old_letters.add(guessed_letter)
            if guessed_letter in word_letter:
                word_letter.remove(guessed_letter)
                print('Great Job, Now pick again.')

            else:
                lives = lives - 1 # Takes away a life if wrong 
                print('\nYour letter, ', guessed_letter, 'is not in the word.')

        elif  guessed_letter in old_letters:
            print('\nYou have already used that letter, Guess again.')

        else: 
            print('\nThat is not a valid letter. ')
        
    # gets here when len(word_letter) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)

    else:
        print('COOL! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()