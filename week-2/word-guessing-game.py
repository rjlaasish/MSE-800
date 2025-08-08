
import random

WORD_LIST = ['Hello','Software','Computer','Yoobee','Auckland']
def get_random_word():
    rd_word = random.choice(WORD_LIST)
    print(rd_word)
    return rd_word

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()


def all_letters_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)



if __name__ == "__main__":
    # while True:
    word = get_random_word()
    lowered_word = word.lower()
    guessed_letters = []
    lives = 3
    
    print('******* Word Guessing Game *******') 
    print(f"You have {lives} lives. Let's begin!\n")
    
    while True:
        print("Word:", display_word(lowered_word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        if len(guess) > 1:
            print('Please guess letter by letter.') 
            continue
        
        if guess in lowered_word:
            print(f"Good job! '{guess}' is in the word.")
            guessed_letters.append(guess)

            if all_letters_guessed(word, guessed_letters):
                print("\nCongratulations! You've guessed the word:", word)
                print("GAME OVER")
                break
        else:
            lives -= 1
            print(f"Wrong guess! You lost a life. Lives remaining: {lives}")
            guessed_letters.append(guess)

            if lives == 0:
                print("\nYou've run out of lives.")
                print("The word was:", word)
                print("GAME OVER")
                break
        