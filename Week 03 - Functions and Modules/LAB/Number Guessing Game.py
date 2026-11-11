import random
true = True
count = 0
number = random.randint(0,100)
guess = float(input("Welcome to guessing game, take your guess (number is between 0-100):"))

while true == True:
    count += 1

    if number == guess:
        print(f"CORRECT!! The number is {number}. You got it in {count} tries.")
        break
    elif guess > 100:
        print ("remember it is lower that 100")
    elif guess < 0:
        print("remember the number is higher than 0")
    elif guess > number:
        print(f"The number is lower than {guess}")
    elif guess < number:
        print(f"The number is higher than {guess}")

    guess = float(input("Take another guess:"))