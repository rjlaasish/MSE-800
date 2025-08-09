import random

class WordGuessingGame:
    WORD_LIST = ['hello', 'software', 'computer', 'yoobee', 'auckland']

    def __init__(self, max_tries):
        self.max_tries = max_tries
        self.lives = self.max_tries
        self.guessed_letters = set()
        self.word = random.choice(self.WORD_LIST).lower()

    def display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def all_letters_guessed(self):
        return set(self.word).issubset(self.guessed_letters)

    def play_game(self):
        print('******* Word Guessing Game *******') 
        print(f"You have {self.lives} lives. Let's begin!\n")

        while self.lives > 0:
            print("\nWord:", self.display_word())
            guess = input("Guess a letter: ").strip().lower()

            if not guess:
                print("Oops! You forgot to enter a letter.\n")
                continue

            if not guess.isalpha() or len(guess) != 1:
                print("Please guess a single letter.\n")
                continue

            if guess in self.guessed_letters:
                print("You've already guessed that letter.\n")
                continue

            self.guessed_letters.add(guess)

            if guess in self.word:
                print(f"Good job! '{guess}' is in the word.")
                if self.all_letters_guessed():
                    print("\nCongratulations! You've guessed the word:", self.word)
                    print("GAME OVER")
                    return
            else:
                self.lives -= 1
                print(f"Wrong guess! You lost a life. Lives remaining: {self.lives}")

        print("\nYou've run out of lives.")
        print("The word was:", self.word)
        print("GAME OVER")

if __name__ == "__main__":
    game = WordGuessingGame(max_tries=5)
    game.play_game()
