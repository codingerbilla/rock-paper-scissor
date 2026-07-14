password = 1234
balance = 100000
pin = int(input("Enter ATM Password: "))

if pin == password:

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter deposit amount: "))
            balance = balance + amount
            print("New Balance =", balance)

        elif choice == 2:
            amount = int(input("Enter withdraw amount: "))
            if amount <= balance:
                balance = balance - amount
                print("New Balance =", balance)
            else:
                print("Insufficient Balance")

        elif choice == 3:
            print("Balance =", balance)

        elif choice == 4:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

else:
    print("Wrong Password")