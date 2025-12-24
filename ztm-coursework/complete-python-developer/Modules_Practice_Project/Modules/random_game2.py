from random import randint


def guessing_game(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print("Congratulations")
                return True
            else:
                print("Wrong answer")
                return False
        else:
            print("Enter only between 1 to 10")
            return False
    except TypeError:
        print("Enter only numbers")
        return False

if __name__ == "__main__":
    computer_choice = randint(1, 10)
    while True:
        try:
            user_choice = int(input(f"Please enter a number between 1 and 10: "))
            if guessing_game(user_choice, computer_choice):
                break
        except ValueError:
            print("Please enter only numbers")
            continue

