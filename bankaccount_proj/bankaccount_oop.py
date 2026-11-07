class Bankaccount:
    def __init__(self,owner,account_no,balance):
        self.owner = owner 
        self.__balance = balance
        self.account_no = account_no


    def __str__(self):#ya __str__ method sirf user ko dikhane ke lia hota hai fancy
        return f"owner:{self.owner} - account no:{self.account_no} - balance:{self.__balance}"
    
    def __repr__(self):# ya bhi __str__ ki tarah hota hai lakin ya developer apne lia banata hai take actual data kia ha ya dekh sake
        return f"onwer name:'{self.owner}':str - account no:'{self.account_no}':str - balance:{self.__balance}:int"

    
    def deposit(self,amount:int):
        if amount <=0:
            print("deposit cannot be 0 or less than zero")
        else:
            self.__balance += amount
    @property # ya propetry aik hidden property ko as a attribute banata hai take ya class ke bahar sirf dikh sake lakin edit nahi karsakte
    def balance(self):
        return self.__balance

    
    def show_balance(self):
        return f"name:{self.owner} balance:{self.__balance}"

    def withdraw(self,amount):
        if int(amount) > self.__balance:
            print(f"your account balance is:{self.__balance} you cannot withdraw higher amount:{amount}")
            return False
        elif int(amount) <=0:
            print("the machine cannot withdraw amount less than or equal to 0")
            return False
        else:
            self.__balance -= int(amount)
            return True

    #def transfer(self,other):
        #pass