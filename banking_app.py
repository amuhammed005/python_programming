def show_balance(balance):
    print(f"\nYour balance is ${balance:.2f}\n")

def deposit():
    try:
        amount = float(input("Enter amount to be deposited: "))
        if amount <= 0:
            print("❌ Deposit amount cannot be greater than 0.\n")
            return 0
        return amount
    except ValueError:
        print("❌ Inavlid input. Please enter a number.\n")
        return 0

def withdraw(balance):
    try:
        amount = float(input("Enter amount to be withdrawed: "))
        if amount > balance:
            print("❌ Withdrawal amount cannot exceed balance.\n")
            return 0
        elif amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.\n")
            return 0
        return amount
    except ValueError:
        print("❌ Inavlid input. Please enter a number.\n")
        return 0

def main():
    print("\n-----------------------------------")
    print("🏦 Welcome to Damsdack Bank.\nWe are always ready to provide your services.")
    print("-----------------------------------\n")

    balance = 0.00
    running = True

    while running:
        print("***** Bank Menu *****")
        print("1.Check Balance \n2.Make Deposit \n3.Make a Withdrawal \n4.Exit Application")

        try:
            choice = int(input("\nEnter 1-4 to make a choice: ").strip())
        except ValueError:
            print("❌ Inavlid choice. Please enter a number between 1 and 4.\n")
            continue
            
        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                running = False
            case _:
                print("❌ Invalid Choice")

if __name__ == "__main__":
    main()