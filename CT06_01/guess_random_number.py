import random

random_num = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == random_num:
    print("Correct!")
else:
    print("Wrong!")
