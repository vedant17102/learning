class BankAccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder=acc_holder
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"amount deposit:{amount}")
        else:
            print('deposit amount cannot be less than 0')
    
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance+=amount
                print(f"amount withdraw:{amount}")
            else:
                print(f'insufficient balance!. Amount withdrawn cannot be greater than original balance')
        else:
            print('withdrawal amount must be greater than 0')

    def check_balance(self):
        return self.balance

b1=BankAccount("vedant",1000) 
print(f'initial balance:{b1.balance}')
b1.deposit(0)
b1.withdraw(1100)
print("final blanace:",b1.check_balance())