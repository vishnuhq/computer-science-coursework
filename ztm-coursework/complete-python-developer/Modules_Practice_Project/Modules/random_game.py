import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])
print("Welcome to the Guessing Game")

while True:
    while True:
        try:
            user_choice = int(input(f"Please enter a number between {start} and {end}: "))
            computer_choice = randint(start,end)
        except ValueError:
            print("Please enter only numbers")
            continue
        break
    print(f"Your choice is {user_choice}")
    print(f"Computer choice is {computer_choice}")
    if user_choice == computer_choice:
        print("Congratulations!! You won!!")
        break
    else:
        print("Uh oh! You guessed it wrong! try again!!")