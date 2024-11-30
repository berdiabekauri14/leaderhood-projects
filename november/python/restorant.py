import time
import random

try:
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
except KeyboardInterrupt:
    quit

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
    
def orders(balance):
    order_list = ["alfredo spaghetti(50$)", "hot potatos(5$)", "tea with cookies(1$)", "mac and cheese(10$)", "fries(2$)", "burger(9$)"]

    print(f"Here is the order list {order_list}")
    order_choose = input("Wich order do you want to have?: ")

    if order_choose != order_list[0] or order_choose != order_list[1] or order_choose != order_list[2] or order_choose != order_list[3] or order_choose != order_list[4] or order_choose != order_list[5]:
        print("Incorrect, You must enter an order wich is in the list")
        order_choose = input("Wich order do you want to have?: ")
    
    if order_choose == order_list[0] and balance >= 50:
        balance - 50
        print(f"You Have bought {order_list[0]}!")
        print(f"Heres your receipt: You have bought {order_list[0]} for {balance}$, Now you have {balance - 50}$")
    elif order_choose == order_list[0] and balance <= 50:
        print(f"Sorry, You dont have enough money to buy that :(")
        order_choose = input("Wich order do you want to have?: ")

    if order_choose == order_list[1] and balance >= 5:
        balance - 5
        print(f"You Have bought {order_list[1]}!")
        print(f"Heres your receipt: You have bought {order_list[1]} for {balance}$, Now you have {balance - 5}$")
    elif order_choose == order_list[1] and balance <= 5:
        print(f"Sorry, You dont have enough money to buy that")
        order_choose = input("Wich order do you want to have?: ")

    if order_choose == order_list[2] and balance >= 1:
        balance - 1
        print(f"You Have bought {order_list[2]}!")
        print(f"Heres your receipt: You have bought {order_list[2]} for {balance}$, Now you have {balance - 1}$")

    if order_choose == order_list[3] and balance >= 10:
        balance - 10
        print(f"You Have bought {order_list[3]}!")
        print(f"Heres your receipt: You have bought {order_list[3]} for {balance}$, Now you have {balance - 10}$")
    elif order_choose == order_list[3] and balance <= 10:
        print(f"Sorry, You dont have enough money to buy that")

    if order_choose == order_list[4] and balance >= 2:
        balance - 2
        print(f"You Have bought {order_list[4]}!")
        print(f"Heres your receipt: You have bought {order_list[4]} for {balance}$, Now you have {balance - 2}$")
    elif order_choose == order_list[4] and balance <= 2:
        print(f"Sorry, You dont have enough money to buy that")

    if order_choose == order_list[5] and balance >= 9:
        balance - 9
        print(f"You Have bought {order_list[5]}!")
        print(f"Heres your receipt: You have bought {order_list[5]} for {balance}$, Now you have {balance - 9}$")
    elif order_choose == order_list[5] and balance <= 9:
        print(f"Sorry, You dont have enough money to buy that")


def main():
    balance = random.randint(1, 100)
    run = True
    
    while run:
        print(f"Welcome back {name} {last_name}, To Berdia's restorant!")
        time.sleep(1.2)
        print("1. Balance")
        print("2. Orders")
        print("3. Exit")

        try:
            choose = int(input("Enter a number between 1-3: "))
        except ValueError:
            print("Incorrect, you must enter a number not an string, please try again")

        if choose == "":
            print("Incorrect, Please fill in the field")

        if choose >= 3:
            print("incorrect, you must enter a number between 1-3")
            choose = int(input("Enter a number between 1-3: "))
        
        if choose == 1:
            show_balance(balance)
        elif choose == 2:
            orders(balance)
        elif choose == 3:
            run = False
            print(f"Thanks for visiting us {name} {last_name}! Come back next time!")
            quit
        else:
            print("That is wrong choise")  
            time.sleep(1.2)

if __name__ == "__main__" :
    main()