def account_creating(account):
    account_holder = input('Enter Account Holder Name: ')
    acccount_number = input('Enter Account Number : ')
    if acccount_number in account :
        print('ALREAADY ACCOUNT NUMBER AVAILABLE')
        return
    account[acccount_number] = {'account_holder' : account_holder,
                                'Balance' : 0.0}
    print("THANKS FOR CREATING AN ACCOUNT")

def deposit_amount(account):
    acccount_number = input('Enter Account Number : ')
    if acccount_number not in account :
       print('Account Number Not Found')
       return
    amount = float(input('Enter Deposit Amount : '))
    if amount >= 0 :
        account[acccount_number]['Balance'] += amount
        print(f"DEPOSITED  {amount} INTO {account[acccount_number]}")
    else :
        print('INVALID DEPOSIT AMOUNT')

def withdraw_amount(account):
    acccount_number = input('Enter Account Number : ')
    if acccount_number not in account :
       print('ACCOUNT NUMBER NOT FOUND')
       return
    w_amount = float(input('Enter Withdraw Amount : '))
    if w_amount >= 0 :
        account[acccount_number]['Balance'] -= w_amount
        print(f"WITHDRAW {w_amount} FROM {account[acccount_number]}")
    else :
        print('INVALID WITHDRAW AMOUNT')

def check_balance(account) :
    acccount_number = input('Enter Account Number : ')
    if acccount_number not in account :
       print('ACCOUNT NUMBER NOT FOUND')
       return
    balance = account[acccount_number]
    print(f"ACCOUNT BALANCE FOR  {acccount_number}:{balance}")

def all_account_show(account)  :
    acccount_number = input('Enter Bank ID : ')
    if acccount_number == '@account' :
        print(f"ALL ACCOUNT ARE {account}")
    else :
        print("INVALID ID ")
         
account = { }

while True :
    print("Enter 1 to Add Account\nEnter 2 to Deposit Amount\nEnter 3 to Withdraw Amount\nEnter 4 to Check Balance\nEnter 5 to All Account Show\nEnter 6 to Exit ")
    choice = int(input("Enter Your Choice Number : "))
    if choice == 1 :
        account_creating(account)
        continue
    elif choice == 2 :
        deposit_amount(account)
    elif choice  == 3 :
        withdraw_amount(account)
    elif choice == 4 :
        check_balance(account)
    elif choice == 5 :
        all_account_show(account)
    elif choice == 6 :
        print("Thanks")
        break
    else :
        print("Invalid Input")