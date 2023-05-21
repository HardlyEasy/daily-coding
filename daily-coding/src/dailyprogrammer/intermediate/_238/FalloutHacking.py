from typing import *
import random

# Hard-coded settings
SETTING_GUESSES = 4
SETTING_FNAME = "popular_words.txt"


class Model:  # Represents an instance of hacking game
    """Instance variable descriptions below
    1) word_bank: all words in txt file
    2) valid_words: valid length words from word bank
    3) game_words: randomly chosen words from valid words
    """
    word_bank = open(SETTING_FNAME, "r").read().splitlines()

    def __init__(self, guesses: int, difficulty: int):
        self.guesses = guesses
        self.difficulty = difficulty
        self.word_length = 4 + difficulty * 2
        self.word_amt = 6 + difficulty * 2
        self.valid_words = self.filter_words()
        self.game_words = self.pick_words()
        self.answer = self.pick_answer()

    def filter_words(self) -> List[str]:
        """Returns words of correct word length from word bank
        Time complexity O(n)
        """
        filtered_words = list()
        for word in Model.word_bank:
            if len(word) == self.word_length:
                filtered_words.append(word)
        return filtered_words

    def pick_words(self) -> List[str]:
        """Returns randomly picked game words from valid words
        """
        game_words = list()
        for i in range(0, self.word_amt):
            game_words.append(
                self.valid_words[random.randint(0, len(self.valid_words))])
        return game_words

    def pick_answer(self) -> str:
        """Returns randomly picked answer word from game words
        """
        return self.game_words[random.randint(0, len(self.game_words))]

    def roll_new(self):
        """Randomly set new answer and game words
        """
        self.game_words = self.pick_words()
        self.answer = self.pick_answer()


class View:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def ask_difficulty() -> int:
        return int(input('Difficulty (0-4)? '))

    def print_words(self):
        for word in self.model.game_words:
            print(word.upper())

    def ask_guess(self) -> str:
        guess = input('Guess ({} left)? '.format(self.model.guesses))
        if guess not in self.model.game_words:
            raise Exception('ask_guess(): Guess word not found in game words')
        return guess


class Controller:  # Managing instances of model and view
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_game(self):
        """Begins game loop of guessing
        """
        self.view.print_words()
        for i in range(0, self.model.guesses):
            guess = self.view.ask_guess()
            correct_amt = self.calc_correct(guess)
            print('{}/{} correct'.format(correct_amt, self.model.guesses))
            if correct_amt == self.model.word_length:
                print('You win!')
                break

    def calc_correct(self, guess):
        correct_amt = 0
        for i in range(0, len(guess)):
            if guess[0] == self.model.answer[0]:
                correct_amt += 1
        return correct_amt


def main():
    model = Model(SETTING_GUESSES, View.ask_difficulty())
    view = View(model)
    controller = Controller(model, view)
    controller.start_game()


if __name__ == '__main__':
    main()
