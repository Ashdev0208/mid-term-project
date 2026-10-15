
# Made by Shodiyor

from studentGrader import student_grader
from guessNumber import guess_number
from ATM import automatic_teller_machine


# -------------------- GREETING --------------------

def greeting():
    print("\n\nWelcome to AshDev playground!")


# -------------------- GET INFORMATION --------------------

def get_info(information):
    info = input(f"Please enter {information}: ")
    return info


# -------------------- RESUME MENU --------------------

def resume():
    while True:
        resume_input = input(
            "\n1. Menu ---------- 2. Log out: "
        )

        if resume_input == "1":
            return "menu"

        elif resume_input == "2":
            return "logout"

        else:
            print("Please enter 1 or 2.")


# -------------------- STUDENT RESULTS --------------------

def iterator(value):
    if not value:
        print("No student results available.")
        return

    count = 0

    for name, grade in value:
        count += 1
        print(f"{count}. Name: {name}; Grade: {grade}")


# -------------------- SHOW ALL RESULTS --------------------

def show_results():
    app = user["apps"]

    print("\n\n========== YOUR RESULTS ==========")

    # Student grader
    print("\n--- Student Grade Manager ---")

    if app["student_grader"]:
        iterator(app["student_grader"])
    else:
        print("Student Grade Manager: empty")

    # ATM
    print("\n--- ATM Simulator ---")

    if app["ATM"]:
        for key, value in app["ATM"].items():

            if key == "history":
                for transaction_number, transaction in value.items():
                    for transaction_type, transaction_value in transaction.items():
                        print(
                            f"Transaction {transaction_number}, "
                            f"{transaction_type}: {transaction_value}"
                        )

            else:
                print(f"{key}: {value}")
    else:
        print("ATM: empty")

    # Guessing game
    print("\n--- Guessing Game ---")

    if not app["guess"]:
        print("Guessing game: empty")

    else:
        for number, result in enumerate(app["guess"], start=1): #it gives us list 
            if isinstance(result, dict):  #it works like type
                print(
                    f"Game {number}: the number was "
                    f"{result['random_number']}, "
                    f"guessed in {result['counter']} attempts."
                )
            else:
                print(f"Game {number}: {result}")


# -------------------- DASHBOARD --------------------

def dashboard():

    app = user["apps"]

    while True:

        print(
            "\n========== ASHDEV PLAYGROUND =========="
            "\n1. Student grade manager"
            "\n2. ATM simulator"
            "\n3. Guessing game"
            "\n4. Show results"
            "\n5. Log out"
        )

        choice = get_info("the number of an application")

        # Student grade manager
        if choice == "1":

            app["student_grader"] = student_grader(
                user["name"],
                user["password"]
            )

            print("\nHere is your student status:")
            iterator(app["student_grader"])

        # ATM simulator
        elif choice == "2":

            app["ATM"] = automatic_teller_machine()

        # Guessing game
        elif choice == "3":

            result = guess_number()

            if result:
                app["guess"].append(result)

            print("\nYour guessing game has finished.")

        # Show results
        elif choice == "4":

            show_results()

        # Log out
        elif choice == "5":

            print("\nYou have logged out.")
            return

        # Invalid choice
        else:

            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 5."
            )
            continue

        # Wait until the user decides what to do next
        action = resume()

        if action == "logout":
            print("\nYou have logged out.")
            return

        # If action == "menu", while True starts the menu again.


# -------------------- LOGIN AND REGISTRATION --------------------

def login(user):

    while True:

        print(
            "\n========== ACCOUNT MENU =========="
            "\n1. Register"
            "\n2. Login"
            "\n3. Exit"
        )

        login_data = get_info("a number")

        # Registration
        if login_data == "1":

            if user["name"]:
                print(
                    "\nYou have already registered. "
                    "Please log in."
                )
                continue

            input_name = get_info("your name")
            input_password = get_info("your password")

            if len(input_name.strip()) < 2:
                print("Your name must contain at least 2 characters.")
                continue

            if len(input_password) < 5:
                print("Your password must contain at least 5 characters.")
                continue

            user["name"] = input_name
            user["password"] = input_password

            print("\nYou have successfully registered!")

            greeting()
            dashboard()

            # When dashboard returns, show the account menu again
            continue

        # Login
        elif login_data == "2":

            if not user["name"]:
                print("\nPlease register before logging in.")
                continue

            input_name = get_info("your name")
            input_password = get_info("your password")

            if (
                input_name == user["name"]
                and input_password == user["password"]
            ):

                greeting()
                print("You have successfully logged in!")

                dashboard()

                # Return to the account menu after logging out
                continue

            else:
                print(
                    "\nIncorrect name or password. "
                    "Please try again."
                )
                continue

        # Exit program
        elif login_data == "3":

            print("\nThank you for using AshDev playground!")
            return

        else:

            print("Invalid choice. Please enter 1, 2, or 3.")


# -------------------- USER DATA --------------------

user = {
    "name": "",
    "password": "",
    "apps": {
        "ATM": 0,
        "student_grader": 0,
        "guess": [],
        "typing": 0
    }
}


# -------------------- START PROGRAM --------------------

greeting()
login(user)
