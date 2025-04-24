import sys
import json

K = "Mr.John"

def show_balance(balance, json_mode=False):
    if json_mode:
        return {"balance": balance, "status": "low" if balance < 5000 else "ok"}
    else:
        if balance < 5000:
            print(K, "Your Current Balance Amount is Low:", balance)
        else:
            print(K, "Your Current Balance Amount is:", balance)

def withdraw_money(balance, amount, json_mode=False):
    if balance >= amount:
        balance -= amount
        if json_mode:
            return {"message": f"Withdrawn {amount}", "balance": balance}, balance
        else:
            print("You have successfully withdrawn", amount)
            show_balance(balance)
            return None, balance
    else:
        if json_mode:
            return {"error": "Insufficient balance."}, balance
        else:
            print("Insufficient balance.")
            return None, balance

def deposit_money(balance, amount, json_mode=False):
    balance += amount
    if json_mode:
        return {"message": f"Deposited {amount}", "balance": balance}, balance
    else:
        print(f"Amount {amount} successfully deposited.")
        show_balance(balance)
        return None, balance

def atm_interactive(balance, pin):
    while True:
        print(f"\n{K} WELCOME TO ATM\n{K} You Have Successfully Logged Into Your Account\n")
        print("""----------------------Main Menu-----------------------
              1 == Balance Inquiry
              2 == Pin Change 
              3 == Fast Cash
              4 == Withdraw Money
              5 == Deposit Money
              6 == Exit From This Account""")
        try:
            choice = int(input("Enter the number which you need from main menu: "))
        except (EOFError, ValueError):
            print("Invalid or no input provided. Exiting.")
            break

        if choice == 1:
            show_balance(balance)

        elif choice == 2:
            confirm = input("Enter YES/NO To Change Your Pin: ")
            if confirm.strip().lower() == "yes":
                try:
                    new_pin = int(input("Enter New Pin (At least 4 digits): "))
                    if len(str(new_pin)) >= 4:
                        pin = new_pin
                        print("You Have Successfully Changed Your Pin")
                    else:
                        print("The Pin Should Be At Least 4 Digits Or More")
                except ValueError:
                    print("Invalid input. Pin must be a number.")

        elif choice == 3:
            try:
                entered_pin = int(input("Enter PIN: "))
                if entered_pin == pin:
                    print("""--------------- Fast Menu To Withdraw Money ----------------
                          1 == 1000
                          2 == 3000
                          3 == 5000
                          4 == 8000
                          5 == More Than 8000""")
                    fast_choice = int(input("Choose option: "))
                    fast_amounts = {1: 1000, 2: 3000, 3: 5000, 4: 8000}
                    
                    if fast_choice in fast_amounts:
                        _, balance = withdraw_money(balance, fast_amounts[fast_choice])
                    elif fast_choice == 5:
                        print("""--------- More Than 8000 Menu ----------
                              1 == 10000
                              2 == 30000
                              3 == 50000
                              4 == 80000
                              5 == 100000""")
                        more_choice = int(input("Choose option: "))
                        more_amounts = {1: 10000, 2: 30000, 3: 50000, 4: 80000, 5: 100000}
                        if more_choice in more_amounts:
                            _, balance = withdraw_money(balance, more_amounts[more_choice])
                        else:
                            print("Invalid option.")
                    else:
                        print("Invalid fast cash option.")
                else:
                    print("Wrong PIN!")
            except ValueError:
                print("Invalid input.")

        elif choice == 4:
            try:
                entered_pin = int(input("Enter Your PIN: "))
                if entered_pin == pin:
                    amount = int(input("Enter the amount to withdraw: "))
                    _, balance = withdraw_money(balance, amount)
                else:
                    print("Wrong PIN!")
            except ValueError:
                print("Invalid amount.")

        elif choice == 5:
            try:
                entered_pin = int(input("Enter Your PIN: "))
                if entered_pin == pin:
                    amount = int(input("Enter the amount to deposit: "))
                    _, balance = deposit_money(balance, amount)
                else:
                    print("Wrong PIN!")
            except ValueError:
                print("Invalid amount.")

        elif choice == 6:
            print("You Have Successfully Logged Out.")
            break

        else:
            print("Invalid choice, please select from the menu.")

def atm_non_interactive(balance, pin, action=None, amount=None):
    result = {}
    if action == "balance":
        result = show_balance(balance, json_mode=True)
    elif action == "withdraw" and amount is not None:
        result, balance = withdraw_money(balance, amount, json_mode=True)
    elif action == "deposit" and amount is not None:
        result, balance = deposit_money(balance, amount, json_mode=True)
    else:
        result = {"error": "Invalid or missing action."}
    print(json.dumps(result))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            user_pin = int(sys.argv[1])
            atm_interactive(100000, user_pin)
        except ValueError:
            print("PIN must be an integer.")
    elif len(sys.argv) >= 3:
        try:
            user_pin = int(sys.argv[1])
            action = sys.argv[2].lower()
            amount = int(sys.argv[3]) if len(sys.argv) == 4 else None
            atm_non_interactive(100000, user_pin, action, amount)
        except ValueError:
            print(json.dumps({"error": "PIN and amount must be integers."}))
    else:
        print("Usage:")
        print("Interactive Mode : python atm.py <pin>")
        print("CI/CD Mode       : python atm.py <pin> <action> [amount]")
