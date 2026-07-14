balance =5000
password_change = "1234"
print("Welcome to the ATM \nPlease enter your password:")
user_password = input()
if user_password == password_change:
    print("Password accepted. What would you like to do?")

    while True:
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Your current balance is: {balance}")
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"You have withdrawn {amount}. Your new balance is: {balance}")
            else:
                print("Insufficient funds.")
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"You have deposited {amount}. Your new balance is: {balance}")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
        break
    else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid Password. Please try again.")
