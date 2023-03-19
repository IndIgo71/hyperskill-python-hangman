import random
from string import ascii_lowercase


class Hangman:
    def __init__(self):
        self.__words = ['python', 'java', 'swift', 'javascript']
        self.goal_word: str = None
        self.current_word = None
        self.__max_attempts = 8
        self.results = {'win': 0, 'lost': 0}
        print()

    def get_hidden_answer(self, guessed_letters):
        hidden_answer = self.goal_word
        diff = set(self.goal_word).difference(guessed_letters)
        for letter in diff:
            if self.goal_word.count(letter) > 0:
                hidden_answer = hidden_answer.replace(letter, '-')
        return hidden_answer

    def get_results(self):
        print(f'You won: {self.results["win"]} times.')
        print(f'You lost: {self.results["lost"]} times.')

    def new_game(self):
        attempt_num = 0
        self.goal_word = random.choice(self.__words)
        guessed_letters = set()
        hidden_answer = self.get_hidden_answer(guessed_letters)
        while True:
            print()
            print(hidden_answer)
            user_input = input('Input a letter: ')

            if user_input not in guessed_letters:
                if len(user_input) != 1:
                    print("Please, input a single letter.")
                elif user_input not in ascii_lowercase:
                    print(
                        "Please, enter a lowercase letter from the English alphabet.")
                elif user_input not in set(self.goal_word):
                    print("That letter doesn't appear in the word.")
                    attempt_num += 1
                else:
                    guessed_letters.add(user_input)
                    hidden_answer = self.get_hidden_answer(guessed_letters)
            else:
                print("You've already guessed this letter.")

            if self.goal_word == hidden_answer:
                self.results["win"] += 1
                print(
                    f'You guessed the word {self.goal_word}!\nYou survived!')

                break
            if attempt_num == self.__max_attempts:
                self.results["lost"] += 1
                print('\nYou lost!')
                break

    def start(self):
        print(f'H A N G M A N')
        while True:
            action = input(
                'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
            if action == 'play':
                self.new_game()
            elif action == 'results':
                self.get_results()
            elif action == 'exit':
                break


if __name__ == '__main__':
    game = Hangman()
    game.start()
