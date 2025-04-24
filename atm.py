import sys

K = "Mr.John"

def show_balance(balance):
    if balance < 5000:
        print(K, "Your Current Balance Amount is Low:", balance)
    else:
        print(K, "Your Current Balance Amount is:", balance)

def atm(balance, pin):
    while True:
        print(K, "WELCOME TO ATM")
        print(K, "You Have Successfully Logged Into Your Account")
        print(K)
        print("""----------------------Main Menu-----------------------
              1 == Balance Inquiry
              2 == Pin Change 
              3 == Fast Cash
              4 == Withdraw Money
              5 == Deposit Money
              6 == Exit From This Account""")
        choice = int(input("Enter the number which you need from main menu: "))

        if choice == 1:
            show_balance(balance)

        elif choice == 2:
            confirm = input("Enter YES/NO To Change Your Pin: ")
            if confirm.lower() == "yes":
                new_pin = int(input("Enter New Pin (At least 4 digits): "))
                if len(str(new_pin)) >= 4:
                    pin = new_pin
                    print("You Have Successfully Changed Your Pin")
                else:
                    print("The Pin Should Be At Least 4 Digits Or More")

        elif choice == 3:
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
                    amount = fast_amounts[fast_choice]
                    if balance >= amount:
                        balance -= amount
                        print("You Have Successfully Withdrawn", amount)
                        show_balance(balance)
                    else:
                        print("Insufficient balance.")
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
                        amount = more_amounts[more_choice]
                        if balance >= amount:
                            balance -= amount
                            print("You Have Successfully Withdrawn", amount)
                            show_balance(balance)
                        else:
                            print("Insufficient balance.")
                    else:
                        print("Invalid option.")
                else:
                    print("Invalid fast cash option.")
            else:
                print("Wrong PIN!")

        elif choice == 4:
            entered_pin = int(input("Enter Your PIN: "))
            if entered_pin == pin:
                amount = int(input("Enter the amount to withdraw: "))
                if balance >= amount:
                    balance -= amount
                    print("You have successfully withdrawn", amount)
                    show_balance(balance)
                else:
                    print("Insufficient balance.")
            else:
                print("Wrong PIN!")

        elif choice == 5:
            entered_pin = int(input("Enter Your PIN: "))
            if entered_pin == pin:
                amount = int(input("Enter the amount to deposit: "))
                balance += amount
                print("Amount successfully deposited.")
                show_balance(balance)
            else:
                print("Wrong PIN!")

        elif choice == 6:
            print("You Have Successfully Logged Out.")
            break

        else:
            print("Invalid choice, please select from the menu.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python atm.py <pin>")
    else:
        try:
            user_pin = int(sys.argv[1])
            atm(100000, user_pin)
        except ValueError:
            print("PIN must be an integer.")
