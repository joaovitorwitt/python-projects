# program that gets the user to generate a secret number for the user guess
import random


def main():
    computer_guess(19)


def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess > random_number:
            print("Too high. Try again")
        elif guess < random_number:
            print("Too low. Try again")
    
    # when guess is equal to random number it breaks out of the loop
    print("That's right")



# function that gets the computer to guess our number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f"The number is {guess}")
    


if __name__ == "__main__":
    main()