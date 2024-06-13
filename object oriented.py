import random


class Hangman:
    player_list = []

    def __init__(self):
        self.name = input("Enter Your Name: ")
        self.__word_list = ["bmw", "benz", "ford", "mostang", "mazerati", "pejo", "pride"]
        self.__win_state = False
        self.tries = 6
        self.player_list.append(self)
        self.word = self.get_word()

    def get_word(self):
        self.word = random.choice(self.__word_list)
        return self.word.upper()

    def play(self):
        word_completion = "_" * len(self.word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        print("Let's play Hangman")
        print("word is name of car!!!")
        print(self.display_hangman())
        print(word_completion)
        print("\n")
        while not guessed and self.tries > 0:
            guess = input("guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("you already tried", guess, "!")
                elif guess not in self.word:
                    print(guess, "isn't in the word :(")
                    self.tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Nice one,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(self.word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(self.word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already tried ", guess, "!")
                elif guess != self.word:
                    print(guess, " ist nicht das Wort :(")
                    self.tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = self.word
            else:
                print("invalid input")
            print(self.display_hangman())
            print(word_completion)
            print("\n")
        if guessed:
            print("Good Job, you guessed the word!")
        else:
            print("I'm sorry, but you ran out of tries. The word was " + self.word + ". Maybe next time!")

    def display_hangman(self):
        stages = ["""
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                       """,
                  """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     /
                       -
                       """,
                  """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |
                       -
                       """,
                  """
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |
                       -
                       """,
                  """
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |
                       -
                       """,
                  """
                       --------
                       |      |
                       |      O
                       |
                       |
                       |
                       -
                       """,
                  """
                       --------
                       |      |
                       |      
                       |
                       |
                       |
                       -
                       """
                  ]
        return stages[self.tries]

    def has_won(self):
        return self.__win_state

    @classmethod
    def game_has_winner(cls):
        if any(player.has_won is True for player in cls.player_list):
            return True
        return False


class GameController:
    def __init__(self):
        while True:
            for player in Hangman.player_list:
                if not player.has_won():
                    player.play()
            if Hangman.game_has_winner():
                break


if __name__ == "__main__":
    while True:
        order = input("what would you like to do? Add, Play or Quit : ")
        if order.upper() == "QUIT":
            break
        elif order.upper() == "PLAY":
            GameController()
        elif order.upper() == "ADD":
            Hangman()

