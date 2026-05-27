from atm.account import display_balance, deposit, withdraw
from atm.transactions import add_transaction, show_statement


def start_menu():

    while True:

        print("\n====== ATM MENU ======")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_balance()

        elif choice == "2":

            amount = float(input("Enter deposit amount: ₹"))

            deposit(amount)

            print("Money Deposited Successfully!")

            add_transaction(f"Deposited ₹{amount}")

        elif choice == "3":

            amount = float(input("Enter withdrawal amount: ₹"))

            success = withdraw(amount)

            if success:
                print("Please collect your cash.")

                add_transaction(f"Withdrawn ₹{amount}")

        elif choice == "4":
            show_statement()

        elif choice == "5":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid Choice! Try Again.")