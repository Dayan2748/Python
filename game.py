print('Welcome to the Number Guessing Game!')
print('Ihave chosen a number between 1 to 100.Try to guess it!')

import random
number_to_guess = random.randint(1,100)

guess = input('Enter Your Guess: ').strip()

if not guess.isdigit():
    print("Please Enter valid Number.")
else:
    guess = int(guess)
    if guess < number_to_guess:
        print("TOO LOW!")
    elif guess > number_to_guess:
        print("TOO HIGH!")
    else :
        print(f"Congratulations! You guessed the number correctly!")

print(f"The number was {number_to_guess}.")
print("Thank You Playing The Number Guessing Game!")