import random


class GuessingGame:
    def __init__(self):
        self.myNum = random.randint(1, 100)
        self.numTries = 1
        print("I just guessed a number between 1 and 100. Show me how many times until you get it right!")
        self.start_game()

    def start_game(self):
        guess = int(input("Enter your guess: "))
        print("You guessed " + str(guess))
        if guess == self.myNum:
            print("Wow you got it right! It took you " + str(self.numTries) + " times")
        elif guess > self.myNum:
            print("Your guess was too high! Try again")
            self.numTries += 1
            self.start_game()
        else:
            print("Your guess was too low! Try again")
            self.numTries += 1
            self.start_game()


if __name__ == '__main__':
    newGame = GuessingGame()
