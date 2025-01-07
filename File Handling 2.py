import os.path

class Account:
    def __init__(self, account_number, account_name, pin, balance):
        self.acc_num = account_number
        self.acc_name = account_name
        self.pin = pin
        self.bal = balance

    def __str__(self):
        return f"Account Number: {self.acc_num}\nAccount Name: {self.acc_name}\nPIN: {self.pin}\nBalance: {self.bal}\n"


def retrieve_account(acc_num):
    with open("Accounts.txt", "r") as file:
        for line in file:
            if line.startswith("Account Number:"):
                existing_account_number = line.split(":")[1].strip()
                if existing_account_number == acc_num:
                    account_info = line.split("\n")[0].split(":")
                    account_name = account_info[1].strip()
                    pin = account_info[2].strip()
                    balance = float(account_info[3].strip())
                    return Account(acc_num, account_name, pin, balance)
    return None


def update_account(account):
    accounts = []
    with open("Accounts.txt", "r") as file:
        for line in file:
            if line.startswith("Account Number:"):
                existing_account_number = line.split(":")[1].strip()
                if existing_account_number == account.acc_num:
                    line = str(account)
            accounts.append(line)

    with open("Accounts.txt", "w") as file:
        for line in accounts:
            file.write(line + "\n")


def main():
    attempts = 0
    while attempts < 3:
        acc_num = input("Enter Account Number: ")
        account = retrieve_account(acc_num)
        if account is None:
            print("Sorry, the Account doesn't exist!")
            attempts += 1
        else:
            pin = input("Enter PIN: ")
            if pin == account.pin:
                print("Welcome to PUP On-Line Banking Systems")
                while True:
                    print("1. Balance Inquiry")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Cancel")
                    transaction = input("Press the desired transaction: ")

                    if transaction == "1":
                        print(f"Your Balance is {account.bal}")

                    elif transaction == "2":
                        try:
                            amount = float(input("Enter Amount: "))
                            if amount > 0:
                                account.bal += amount
                                update_account(account)
                                print("Deposit successful.")
                            else:
                                print("Invalid amount. Deposit failed.")
                        except ValueError:
                            print("Invalid amount. Deposit failed.")

                    elif transaction == "3":
                        try:
                            amount = float(input("Enter Amount: "))
                            if 0 < amount <= account.bal:
                                account.bal -= amount
                                update_account(account)
                                print("Withdrawal successful.")
                            else:
                                print("Invalid amount. Withdrawal failed.")
                        except ValueError:
                            print("Invalid amount. Withdrawal failed.")

                    elif transaction == "4":
                        print("End of Program")
                        return

                    else:
                        print("Invalid transaction. Please try again.")

            else:
                print("Incorrect PIN. Please try again.")
                attempts += 1

    print("Maximum attempts exceeded. Exiting the program.")


if __name__ == "__main__":
    if not os.path.isfile("Accounts.txt"):
        with open("Accounts.txt", "w") as file:
            pass
    main()
