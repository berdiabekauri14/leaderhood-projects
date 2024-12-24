import random
import time

try:
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
except KeyboardInterrupt:
    print("Goodbye!")
    
number_list = [i for i in range(1, 101)]
secret_number = random.choice(number_list)

print(f"Welcome back {name} {last_name} to guess the number game!".title())
time.sleep(1.2)
print("Here are the rules you will need for the game".title())
time.sleep(1.2)
print("1. if you see 🟢🟢🟢 squares, this means the number is correct".title())
time.sleep(1.2)
print("2. if you see 🔴🔴🔴 squares, this means the number is incorrect".title())
time.sleep(1.2)
print("You have 3 chances, you can try again 1 time!".title())
time.sleep(1.2)

def start():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("incorrect, you must enter a number not an string".title())
        num = int(input("Enter a number: "))

    if num == secret_number:
        print("🟢🟢🟢")
        print("You guessed the number!".title())
        quit
    elif num > secret_number:
        print("number is big, make it a lower number".title())
    elif num < 0:
        print("incorrect, number must be positive".title())
    else:
        print("🔴🔴🔴")

def exit():
    print(f"Good bye {name} {last_name}, Have a great day!")
    quit

def try_again():
    accept2 = int(input("Do you want to try again? (1 - yes, 2 - no): "))

    if accept2 == 1:
        for i in range(3):
            start()
    
    if accept2 == 2:
        exit()

def game():
    try:
        accept = int(input("Do you want to start the game? (1 - yes, 2 - no): "))
    except ValueError:
        print("incorrect, you must enter a number not an string".title())
        accept = int(input("Do you want to start the game? (1 - yes, 2 - no): "))

    if accept == 1:
        for i in range(3):
            start()
        secret_number = random.choice(number_list)
        print(f"The Number was {secret_number}".title())
        try_again()

    if accept == 2:
         exit()

game()