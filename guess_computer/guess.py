# program that gets the user to generate a secret number for the user guess
import random

random_number = random.randint(1, 10)

print(f"THE SECRET NUMBER IS: {random_number}")

user_guess = int(input("GUESS THE NUMBER: "))

while user_guess != random_number:
    print("TRY AGAIN")
    user_guess = int(input("GUESS THE NUMBER: "))

    if user_guess == random_number:
        print("CONGRATULATION YOU GOT IT")
        break
