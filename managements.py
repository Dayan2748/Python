id = input("Enter Your ID : ")
password = input("Enter Password : ")
if id == "Inventory MGT" and password == 'inv12345' :
    print("You Can Access Application")
    vegetables = []
    fruits = []
    while True:
        a = input("Enter an item/'current' to check your items/'final' to get result : ").strip().lower()
        if a == 'current':
            print('fruits = ',fruits)
            print('vegetables = ',vegetables)
            continue
        elif a == 'final':
            print('fruits = ',fruits)
            print('vegetables = ',vegetables)
            break
        else:
            b = input('Enter the item is "fruit  / vegetable" : ').strip().lower()
            if b == 'fruit' :
                fruits.append(a)
            elif b == 'vegetable' :
                 vegetables.append(a)
            else :
                print("Invalid Input!")
elif id == 'Cafe MGT' and password == 'cafe7890' :
    print("Menu \n Pizza : 50$ \n Burger  : 20$ \n Pasta : 25$ \n Momo's : 20$ \n Sandwich : 24$")
    menu = {
        "Pizza" : 50, 
         "Burger" : 20, 
         "Pasta" :25 ,
         "Momo's" : 20, 
         "Sandwich" : 24}
    total_order = 0
    item1 = input("Enter Your Item To Order : ")
    if item1 in menu:
        total_order += menu[item1]
        print(f"Your Item is {item1} added to your order list.")
    else:
        print("Your item is not available!")
    another_item = input("Enter Your Second Item To Order (Not Order write'no'): ")
    if another_item in menu :
        total_order += menu[another_item]
        print(f"Your Item is {another_item} added to your order list.")
        print(f"Total Bill = {total_order}")
        print("Thank You")
    elif another_item == 'no' :
        print(f"Total Bill = {total_order}")
        print("Thank You")
    else:
        print("This Item Is Not In Menu ")
        print("Please Check The Menu")
elif id == 'Student MGT'  and password == 'stu12234':
    def student_grade():

        students = { }

        def  add_student(name,grade):
            students[name] = [grade]
            print(f"Student Name is {name} and Grade is {grade}")

        def update_student(name,grade):
            if name in students:
                students[name] = [grade]
                print(f"Student Name is {name} and update grade is {grade}")
            else:
                print('Not found students')

        def delete_student(name,grade):
            if name in students:
                del students[name]
            else:
                print(f"Not found students!")

        print('Press 1 to add new student')
        print('Press 2 to update student')
        print('Press 3 to delete student')
        print('Press 4  to check given students')
        print('Press 5 get final results all students')

        while True :
            choice = int(input("Enter Your Choose Number: "))

            if choice == 1:
                name = input('Enter student name: ')
                grade = input('Enter student grade: ')
                add_student(name, grade)
                continue

            elif choice == 2 :
                name = input('Enter student name: ')
                grade = input('Enter student grade: ')
                update_student(name, grade)

            elif choice == 3 :
                name = input('Enter student name: ')
                grade = input('Enter student grade: ')
                delete_student(name, grade)

            elif choice  == 4 :
                print(students)

            elif choice == 5 :
                print(students)
                break

            else :
                print('Not Found')
    student_grade()
elif id == "Bank MGT" and password == "bank4567" :
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

else :
    print("Please Enter Valid ID and Password")