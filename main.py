# main.py
# computer will guess the number user picks
import random


# BELOW used by guessTheNumber_computer_game
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Number 1 to {x}? "))
        if guess < random_number:
            print("Sorry. too low.")
        elif guess > random_number:
            print("Sorry. too high.")
    print(f"Correct! Number is {random_number}.")

def computer_guess(x):
    low = 1
    high = x # upperbound number
    feedback = ''
    # while feedback != 'c' and low != high: # optional
    while feedback != 'c':
        # if low == high: # only adds 1 to low
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high because low == high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct(C)?? ').lower()
        if feedback == 'h': # sets upperbound of guess
            high = guess - 1
        elif feedback == 'l': # sets lowerbound of guess
            low = guess + 1
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

# guess(10) # used by guessTheNumber_computer
computer_guess(50)


