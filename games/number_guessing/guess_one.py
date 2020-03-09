import random

playing = True

while playing:
    secret_number = random.randint(0, 100)

    guesses_left = 5
    guessed_correctly = False

    while not guessed_correctly:
        if guesses_left > 0:
            guess = input("What number am I thinking of? ")
            guesses_left -= 1

            if secret_number == int(guess):
                print("Yay! You got it.")
                guessed_correctly = True
            elif secret_number > int(guess):
                print("Think bigger.")
            else:
                print("Think smaller.")
        else:
            print("You lose! the number was ", secret_number)
            break

    print("Good job! you played a game.")

    play_again = input("Would you like to play again? (y or n)")
    if play_again.lower().startswith('y'):
        playing = True
    else:
        playing = False
