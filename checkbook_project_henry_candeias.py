import os

# Function to initialize the ledger file if it doesn't exist
def initialize_ledger(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as ledger_file:
            ledger_file.write("0.00")  # Initialize with a balance of $0.00

# Function to view the current balance
def view_balance(filename):
    with open(filename, "r") as ledger_file: # Reads balance first and casts it to a float type
        balance = float(ledger_file.read())
        return balance

# Function to record a debit (withdrawal)
def record_debit(filename, amount):
    with open(filename, "r") as ledger_file: # Reads balance first and casts it to a float type
        balance = float(ledger_file.read())
    with open(filename, "w") as ledger_file: # Writes in the new calculated balance to the ledger after the debit is recorded
        new_balance = balance - amount
        ledger_file.write(f"{new_balance:.2f}")

# Function to record a credit (deposit)
def record_credit(filename, amount):
    with open(filename, "r") as ledger_file: # First reads the ledger file and casts the balance as a float type
        balance = float(ledger_file.read())
    with open(filename, "w") as ledger_file: # Writes in new calculated balance to the ledger after the credit is recorded
        new_balance = balance + amount
        ledger_file.write(f"{new_balance:.2f}")

# Main function to run the checkbook application
def main():
    ledger_file = "ledger.txt"
    initialize_ledger(ledger_file)

    print("~~~ Welcome to your terminal checkbook! ~~~") # Welcomes user to checkbook

    # Prints all the possible actions for the user
    while True: 
        print("\nWhat would you like to do?\n")
        print("1) View current balance")
        print("2) Record a debit (withdraw)")
        print("3) Record a credit (deposit)")
        print("4) Exit")

        choice = input("\nYour choice? ") # asks for user input

        if choice == "1":
            balance = view_balance(ledger_file)
            print(f"Your current balance is ${balance:.2f}.") # Allows user to see their printed balance to the accuracy of two decimal places
        elif choice == "2":
            debit = float(input("\nHow much is the debit? $")) # Asks how much the user would like to debit
            record_debit(ledger_file, debit)
        elif choice == "3":
            credit = float(input("\nHow much is the credit? $")) # Asks how much the user would like to credit
            record_credit(ledger_file, credit)
        elif choice == "4":
            print("\nThanks, enjoy the rest of your day!") # Allows the user to exit the program if choice 4 is selected
            break
        else:
            print("\nInvalid choice. Please select a valid option (1-4).") # Prompts user to input a valid option

if __name__ == "__main__": # Checks to see if the script is being ran as the main program or being imported as a module in another script
    main()
