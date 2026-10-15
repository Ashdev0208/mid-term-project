# made by Shodiyor 26012935

# ----- export funcion
def automatic_teller_machine():
    # it is for date saving 
    from datetime import datetime as dt
    print("it is in the test mode!\nso enter any kind of card number\n")
    personal_data = {"card_number": 0,"pin": 0,"balance":1000,"history": {}}



    # it is for menu
    def menu():
        while True:
            print(
                "1. Check Balance\n"
                "2. Withdraw\n"
                "3. Deposit\n"
                "4. Transfer\n"
                "5. Transaction History\n"
                "6. Exit"
            )

            value = input("Enter the number: ")

            if not value.isdigit():
                print("Please enter numbers only.")
                continue

            value = int(value)

            if 1 <= value <= 6:
                return value

            print("Please enter a number from 1 to 6.")

            
    # it helps the project to send information to main pyhton
    def historySaver(what):
        now = f"{dt.now().hour}:{dt.now().minute}:{dt.now().second}:{dt.now().microsecond}"
        personal_data['history'][now] = what
    # transfers
    def transfer():
        amount = 0
        
        while True:
            recipientNumber = input("Please enter a card number: ")
            if len(recipientNumber) < 6 or not recipientNumber.isdigit():
                print("Card number must contain at least 6 digits or enter numbers only")
                continue
            value = input("please enter the amount: ")
            if not value.isdigit():
                print("please enter the amount only numbers")
                continue
            value = int(value)

            if personal_data['balance'] >= value and value > 0:
                personal_data["balance"] -= value
                amount = value
                break
            else:
                print("enter the amount that you have or positive numbers only")
        historySaver({"card number": recipientNumber,"Amount": amount})
        print(f"you have successfully transferred ({recipientNumber}: {amount})")
    # deposit
    def deposit():
        while True:
            print("warning: the amount must be higher than 10 and lower than 500")
            depositValue = input("please enter the deposit amount")
            if not depositValue.isdigit():
                print("please enter the amount only numbers")
                continue
            depositValue = int(depositValue)
            if 500 > depositValue > 10:
                personal_data["balance"] += depositValue
                print(f"you have successfully deposited ({depositValue})  into your balance")
                historySaver({"deposited Value": depositValue})
                break
            else:
                print("please follow the rule")
                continue
    # exit handler 
    def exit_handler():
        print("1. Menu --- 2. Dashboard")
        data = input("Enter the number: ")

        if data == "1":
            return "menu"
        elif data == "2":
            return personal_data
        else:
            print("Please enter 1 or 2.")
            return exit_handler()

    # withdraw
    def withdraw():
        while True:
            money = input("how much do you withdraw: ")
            if not money.isdigit():
                print("please enter the amount only numbers")
                continue
            money = int(money)
            if money <= 0:
                print("please enter positive numbers")
                continue
            elif personal_data["balance"] < money:
                print("oops, you dont have enough money to widthraw")
                print("1. try again --- 2. menu")
                number = input("enter the number: ")
                if not number.isdigit():
                    print("please enter the amount only numbers")
                    continue
                number = int(number)
                if number == 1:
                    continue
                elif number == 2:
                    hero_section()
                else:
                    print("please enter those numbers")
            else:
                personal_data["balance"] -= money
                historySaver({"withdrawed Amount": money})
                print(f"Successfully withdrawn {money}.")
                print(f"you have succesfully withdrawed the money ({personal_data['balance']})")
                return


    # main section
    def hero_section():
        while personal_data["card_number"] == 0 or personal_data["pin"] == 0:
            card_information = input("Please enter your card number: ")
            card_pin = input("Please enter your PIN: ")

            if (
                len(card_information) >= 6
                and len(card_pin) >= 4
                and card_information.isdigit()
                and card_pin.isdigit()
            ):
                personal_data["card_number"] = card_information
                personal_data["pin"] = card_pin
                print("You have successfully entered your bank account!")
            else:
                print("Please enter your information correctly.")

        while True:
            command = menu()

            if command == 1:
                print(f"Your balance is {personal_data['balance']}.")

            elif command == 2:
                withdraw()

            elif command == 3:
                deposit()

            elif command == 4:
                transfer()

            elif command == 5:
                if not personal_data["history"]:
                    print("No transactions yet.")
                else:
                    for time, transaction in personal_data["history"].items():
                        for key, value in transaction.items():
                            print(time, key + ":", value)

            elif command == 6:
                print("Thank you for using our ATM!")
                return personal_data
    data = hero_section()
    return data

