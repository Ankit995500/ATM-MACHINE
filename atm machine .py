balance = 50000
pin = "2547004"

print("===== Welcome to CGC ATM =====")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    while True:
        print("\n----- MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print("Your current balance is:", balance)

        elif choice == "2":
            deposit = float(input("Enter amount to deposit: "))
            if deposit > 0:
                balance += deposit
                print("Deposit successful!")
            else:
                print("Invalid amount!")

        elif choice == "3":
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw <= balance and withdraw > 0:
                balance -= withdraw
                print("Withdrawal successful!")
            else:
                print("Insufficient balance or invalid amount!")

        elif choice == "4":
            print("Thank your visit 🙏")
            break

        else:
            print("Invalid choice! Try again.")

else:
    print("Incorrect PIN! Access denied ❌")