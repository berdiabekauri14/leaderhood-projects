import time

try:
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
except KeyboardInterrupt:
    quit

try:
    age = int(input("Enter your age: "))
    ID_number = int(input("Enter your ID number: "))
except ValueError:
    print("incorrect, you must enter a number not an string. please try again".title())
    age = int(input("Enter your age: "))
    ID_number = int(input("Enter your ID number: "))

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}".title())
    
def deposit():
    amount = float(input("Enter an amount which you want to be deposited: "))
    if amount < 0:
        print("incorrect number, number must be positive".title())
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdraw: "))
    if amount > balance:
        print("funds are unsufficient".title())
        return 0
    elif amount < 0:
        print("incorrect amount, amount should be more than 0".title())  
        return 0  
    else:
        return amount    

def loop():
    balance = 0
    run = True
    
    while run:
        print(f"Welcome {name} {last_name} To Berdia's Bank!".title())
        time.sleep(1.2)
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choose = int(input("Enter number between 1-4: "))
        except ValueError:
            print("Incorrect, you must enter a number not an string, please try again".title())

        if choose == "":
            print("incorrect, please fill in the field".title())

        if choose == 1:
            show_balance(balance)
        elif choose == 2:
            balance += deposit()    
        elif choose == 3:
            balance -= withdraw(balance)  
        elif choose == 4:
            run= False
        else:
            print("that is wrong choise".title())    
    print("Thank You For visiting us! have a great day :)".title())

if __name__ == "__main__" :
    loop() 