import random
import time

name = input("Enter your name: ")
last_name = input("Enter your last name: ")

print(f"Welcome back, {name.capitalize()} {last_name}, To rock paper scissors!")
time.sleep(1.5)

def start():
    choices = ["rock", "paper", "scissors"]
    your_choice = input("Enter your choice: ")
    computer_choice = random.choice(choices)

    your_score = 0
    computer_score = 0

    if your_choice != choices[0] or your_choice != choices[1] or your_choice != choices[2]:
        print("Incorrect, You must enter 'rock' or 'paper' or 'scissors'")
        your_choice = input("Enter your choice: ")

    if your_choice == choices[0] and computer_choice == choices[1]:
        computer_score += 1
        print(f"Your score: {your_score}")
        print(f"Computers score: {computer_score}")
        print(f"You lost! The computers choice was {choices[1]}")

    elif your_choice == choices[1] and computer_choice == choices[0]:
        your_score += 1
        print(f"Your score: {your_score}")
        print(f"Computers score: {computer_score}")
        print(f"You won! The computers choice was {choices[0]}")

    elif your_choice == choices[0] and computer_choice == choices[2]:
        your_score += 1
        print(f"Your score: {your_score}")
        print(f"Computers score: {computer_score}")
        print(f"You won! The computers choice was {choices[2]}")

    elif your_choice == choices[2] and computer_choice == choices[0]:
        computer_score += 1
        print(f"Your score: {your_score}")
        print(f"Computers score: {computer_score}")
        print(f"You lost! The computers choice was {choices[0]}")

    elif your_choice == choices[1] and computer_choice == choices[2]:
        computer_score += 1
        print(f"Your score: {your_score}")
        print(f"Computers score: {computer_score}")
        print(f"You lost! The computers choice was {choices[2]}")

    elif your_choice == choices[2] and computer_choice == choices[1]:
        your_score += 1
        print(f"Your score: {your_score}")
        print(f"Computers score: {computer_score}")
        print(f"You won! The computers choice was {choices[1]}")
        
    else:
        print(f"Your score: {your_score}")
        print(f"Computers score: {computer_score}")
        print("Draw!")

def exit():
    print(f"Goodbye, {name.capitalize()} {last_name}, Come back next time!")
    quit

def try_again():
    try:
        accept2 = int(input("Do you want to try again? (1(yes), 2(no)): "))
    except ValueError:
        print("Incorrect, Must enter an number not an string, Please try again")

    if accept2 == 1:
        start()

    if accept2 == 2:
        exit()  

def game():
    try:
        accept = int(input("Do you want to start the game? (1 - Yes, 2 - No): "))
    except ValueError:
        print("Incorrect, You must enter a number not an string, Please try again")
        time.sleep(1.5)
        accept = int(input("Do you want to start the game? (1 - Yes, 2 - No): "))

    if accept > 2:
        print("Incorrect, Must enter 1(yes) or 2(no)")
        accept = int(input("Do you want to start the game? (1 - Yes, 2 - No): "))
    
    if accept == 1:
        for i in range(3):
            start()
        try_again()
    
    if accept == 2:
        exit()

if __name__ == "__main__":
    game()