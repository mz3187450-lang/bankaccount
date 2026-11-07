from bankaccount_oop import Bankaccount

def add_account(account:list):
    
    name = input("enter your name:")
    while True:
        account_nu = input("enter account_no:")
        balance = input("enter balance:")

        if account_nu.isdigit() and balance.isdigit():
            account_exist = True
            for acc in account:
                if acc.account_no == account_nu:
                    print("same account number cannot be add")
                    account_exist = False
            
            if account_exist == False:
                continue
            break
        elif account_nu.isdigit() and not balance.isdigit():
            print("balance is not in digit")
        elif not account_nu.isdigit() and balance.isdigit():
            print("account number is not in digit")
        elif not account_nu.isdigit() and not balance.isdigit():
            print("account no and balance no both are not in digits")
 

    acc = Bankaccount(name,account_nu,int(balance))
    account.append(acc)
def list_account(account:list):
    if len(account) == 0:
        print("ther is no account registered")
    else:
        for i in account:
            print(i)
def transfer(account:list):
    pass
def deposit(account:list):
    account_no = input("enter your account no:")
    checker = True
    for acc in account:
        if acc.account_no == account_no:
            amount = int(input("enter amount you want to deposit:"))
            acc.deposit(amount)
            checker = False
    if checker == True:
        print("account cannot found") 


def withdraw(account:list):
    account_no = input("enter your account no:")
    checker = True

    for acc in account:
        if account_no == acc.account_no:
            amount = input("enter amount you want to withdraw:")
            acc.withdraw(amount)
            checker = False   
    if checker == True:
            print("account is not found")

def show_balance(account):
    account_no = input("enter account no:")
    checker = True
    for acc in account:
        if acc.account_no == account_no:
            checker = False
            return acc.show_balance()
    if checker == True:    
        print("account number cannot be match")
def transfer(account):
    account1 = input("enter your account no:")
    checker = True
    for acc in account:
        if acc.account_no == account1:
            checker = False
            account2 = input("enter 2nd person account:")
            checker2 = True
            for acc2 in account:
                if acc2.account_no == account2:
                    checker2 = False
                    amount = int(input("enter amount to transfer:"))
                    result = acc.withdraw(amount)
                    if result == True:
                        acc2.deposit(amount)
                        print("money transfer successfully")
                    else:
                        print("Transaction fail")
            if checker2 ==True:
                    print("2nd person account is wrong")
    if checker ==True:
            print("your account number is wrong")



    