from bankaccount_func import add_account
from bankaccount_func import list_account
from bankaccount_func import withdraw
from bankaccount_func import show_balance
from bankaccount_func import deposit
from bankaccount_func import transfer
account =[]
if __name__ =="__main__":
    while True:
         print("========= Account Menu =========")
         print("1:Add account")
         print("2:list account")
         print("3:withdraw")
         print("4:show balance")
         print("5:deposit")
         print("6:transfer")
         print("7:exit")
         choice = input("enter number:")
         if choice == "1":
             add_account(account)
         elif choice == "2":
             list_account(account)
         elif choice == "3":
             withdraw(account)
         elif choice == "4":
             balance = show_balance(account)
             print(balance)
         elif choice =="5":
             deposit(account)
         elif choice == "6":
             transfer(account)
         elif choice == "7":
             print("Bye!")
             break
         else:
             print("you enter wrong option")

   