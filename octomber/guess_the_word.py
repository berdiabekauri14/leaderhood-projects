import random
import time

try:
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
except KeyboardInterrupt:
    print("Goodbye!")
    
words = ["python", "squad", "rainbow", "brain", "country", "dragon", "couch", "light", "goverment", "bird", "eagle", "camera", "police", "bunny", "dog", "cat", "fox", "marker", "drawing", "captain", "women", "corn"]
word = random.choice(words)

print(f"Welcome back {name} {last_name} to guess the word!".title())
time.sleep(1.2)
print("Here are the rules you will need for the game".title())
time.sleep(1.2)
print("1. if you see 🟩🟩🟩 squares, this means the word is correct".title())
time.sleep(1.2)
print("2. if you see 🟥🟥🟥 squares, this means the word is incorrect".title())
time.sleep(1.2)
print(f"The Words In List Are: {words}")
time.sleep(1.2)
print("You have 3 chances, Dont lose them!. You can try again 1 time".title())
time.sleep(1.2)

def start():
    try:
        wor = input("Enter a word: ")
    except ValueError:
        print("incorrect, you must enter a string not an number".title())
        wor = input("Enter a word: ")

    if wor == "":
        print("incorrect, please fill the field".title())

    if wor == word:
        print("🟩🟩🟩")
        print("You win!".title())
        quit
    else:
        print("🟥🟥🟥")

def exit():
    print(f"Good bye {name} {last_name}, Have a great day!".title())
    quit

def try_again():
    try:
        accept2 = int(input("Do you want to try again? (1 - yes, 2 - no): "))
    except ValueError:
        print("Incorrect, you must enter a number not an string".title())

    if accept2 == "":
        print("incorrect, please fill the field".title())
        accept2 = int(input("Do you want to try again? (1 - yes, 2 - no): "))

    if accept2 == 1:
        for i in range(3):
            start()

        print(f"The Word Was '{word}'!")

    if accept2 == 2:
        exit()

def game():
    try:
        accept = int(input("Do you want to start The game? (1 - yes, 2 - no): "))
    except ValueError:
        print("incorrect, you must enter a number not an string".title())
        accept = int(input("Do you want to start The game? (1 - yes, 2 - no): "))

    if accept == 1:
        for i in range(3):
            start()
        word = random.choice(words)
        print(f"The Word Was '{word}'!")
        try_again()

    if accept == 2:
        exit()

game()