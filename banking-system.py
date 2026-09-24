import random
from datetime import datetime


accounts = {}

def generate_account_number():
    account_number = random.randint(100000, 999999)
    existing_account_number = accounts.keys()
    if account_number not in existing_account_number:
        return account_number
    else:
        return generate_account_number()


def create_account():
    name = input('Name: ')
    pin = input('Pin: ')

    while not(pin.isdigit() and len(pin)==4):
        print('PIN must be exactly 4 digits')
        pin = input('Pin: ')

    account_number = generate_account_number()

    opening_deposit = None
    while opening_deposit is None:
        try:
            amount = float(input('Opening Deposit: '))
            if amount<0:
                print('Amount must be non-negative')
            else:
                opening_deposit = amount
        except ValueError:
            print('Amount must be a number')
            
    accounts[account_number] = {
            'name': name,
            'pin': pin,
            'balance': opening_deposit,
            'transaction_history': []
    }
    print('Account Number:', account_number)


def login():
    try:
        account_number = int(input('Account Number: '))
        if account_number not in accounts.keys():
            print('Invalid Account Number')
            return None
    except ValueError:
        print('Account Number is a number')
        return None

    for attempt in range(3):
        pin = input('Pin: ')
        if pin == accounts[account_number]['pin']:
            return account_number
        else:
            print('Invalid Pin')

    print('Pin is incorrect! Try again later')
    return None


def check_balance(acc_no):
    print('Balance:', accounts[acc_no]['balance'])


def deposit(acc_no):
    amount = None
    while amount is None:
        try:
            value = float(input('Enter amount: '))
            if value > 0:
                amount = value
            else:
                print('Amount must be non-negative')
        except ValueError:
            print('Amount must be a number')
    
    accounts[acc_no]['balance'] += amount
    transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deposited: {amount}"
    accounts[acc_no]['transaction_history'].append(transaction)

    print(f"Deposited {amount}. New balance: {accounts[acc_no]['balance']}")


def withdraw(acc_no):
    amount = None
    while amount is None:
        try:
            value = float(input('Enter amount'))
            if (value > 0) and (value <= accounts[acc_no]['balance']):
                amount = value
            else:
                print('Amount must be non negative number less than or equal to the balance available')
        except ValueError:
            print('Amount must be a number')

    accounts[acc_no]['balance'] -= amount
    transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdrawn: {amount}"
    accounts[acc_no]['transaction_history'].append(transaction)
    
    print(f"Withdrawn {amount}. New balance: {accounts[acc_no]['balance']}")    


def transfer(acc_no):
    rec_acc_no = None
    while rec_acc_no is None:
        try:
            entered = int(input("Recipient's account number: "))
            if entered not in accounts.keys():
                print('Recipient account does not exist')
            elif entered == acc_no:
                print('Cannot transfer to your own account')
            else:
                rec_acc_no = entered
        except ValueError:
            print('Account Number must be a number')

    amount = None
    while amount is None:
        try:
            value = float(input('Amount to transfer: '))
            if (value > 0) and (value <= accounts[acc_no]['balance']):
                amount = value
            else:
                print('Amount must be a non-negative number less than or equal to the balance available')
        except ValueError:
            print('Amount must be a Number')
    
    accounts[acc_no]['balance'] -= amount
    accounts[rec_acc_no]['balance'] += amount

    transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdrawn: {amount}"
    accounts[acc_no]['transaction_history'].append(transaction)

    transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deposited: {amount}"
    accounts[rec_acc_no]['transaction_history'].append(transaction)


def view_history(acc_no):
    transactions = accounts[acc_no]['transaction_history']
    if not transactions:
        print('No transactions to show')
    else:
        for transaction in transactions:
            transaction_timestamp, rest = transaction.split(' - ', 1)
            transaction_type, transaction_amount = rest.split(':', 1)

            print('-'*30)
            print('Type:', transaction_type.strip())
            print('Timestamp:', transaction_timestamp.strip())
            print('Amount:', transaction_amount.strip())


def change_pin(acc_no):
    pin = None
    while pin is None:
        entered = input('Pin: ')
        if entered!=accounts[acc_no]['pin']:
            print('Incorrect pin. Try Again')
        else:
            pin = entered

    new_pin = input('Pin: ')
    while not(new_pin.isdigit() and len(new_pin)==4):
        print('PIN must be exactly 4 digits')
        new_pin = input('Pin: ')

    re_enter_new_pin = input('Re-enter Pin: ')
    while new_pin!=re_enter_new_pin:
        print('New Pin doesn\'t match')
        re_enter_new_pin = input('Re-enter Pin:')

    accounts[acc_no]['pin'] = new_pin


def account_menu(acc_no):
    while True:
        print("""ACCOUNT MENU
        1. Check Balance
        2. Deposit
        3. Withdraw
        4. Transfer
        5. Transaction History
        6. Change PIN
        7. Logout
        """)
        try:
            value = int(input('Enter Choice: '))
            if (value<=7) and (value>=1):
                choice = value
            else:
                print('Enter a number between 1 and 7')
        except ValueError:
            print('Enter a number')
        else:
            match choice:
                case 1:
                    check_balance(acc_no)
                case 2:
                    deposit(acc_no)
                case 3:
                    withdraw(acc_no)
                case 4:
                    transfer(acc_no)
                case 5:
                    view_history(acc_no)
                case 6:
                    change_pin(acc_no)
                case 7:
                    break


def main_menu():
    while True:
        print("""MAIN MENU
        1. Create account
        2. Login
        3. Exit
        """)
        try:
            value = int(input('Enter Choice: '))
            if (value<=3) and (value>=1):
                choice = value
            else:
                print('Enter a number between 1 and 3')
        except ValueError:
            print('Enter a number')
        else:
            match choice:
                case 1:
                    create_account()
                case 2:
                    acc_no = login()
                    if acc_no is not None:
                        account_menu(acc_no)
                case 3:
                    break


if __name__ == "__main__":
    main_menu()