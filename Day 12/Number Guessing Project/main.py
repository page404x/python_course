import art
import random
print (art.logo)


def random_number():
    number = random.randint(1,100)
    return number

def guess_number(guess):
    if guess < number:
        print("Your guess is too low")
        exit = False

    elif guess > number:
        print("Your guess is too high")
        exit = False
    else:
        print("You're correct")
        exit = True
    return exit

number = random_number()

difficult = input("Do you want to play in easy or hard mode?").lower()

if difficult == "hard":
    retry = 5
else:
    retry = 10

remaining = retry
exit = False

while remaining >= 1 and exit == False:
    print(f"you have {remaining} try")
    guess_num = int(input("Please guess a number?"))
    exit = guess_number(guess_num)
    remaining -= 1

