# Program to create bank account.

class Account():
    def __init__ (self , owner, balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,balance):
        self.balance=self.balance+balance
        return (f'{balance} has been deposited to {self.owner} account'+'\n'+f'Your current balance is {self.balance}')

    def withdraw(self,balance):
        if self.balance<balance:
            return (f'{self.owner} not enough balance in your account')
        else:
            self.balance=self.balance-balance
            return (f'{self.owner} you withdraw {balance} money from your bank account'+'\n'+f'Your current balance is {self.balance}')

    def __str__(self):
        return (f' Account owner: {self.owner}\n Account Balance: {self.balance}')

a=True
while a:
    choice_1= input('You want to open your bank account(y/n):')
    if choice_1.lower() == 'y':
        owner = input("Enter the owner's name:")
        balance=0
        acct_1 = Account(owner,balance)
        b=True
        while b:
           print('\t\tYOUR CHOICES')
           print('1. Deposit money')
           print('2. Withdraw money')
           print("3. Owner's name")
           print('4. Account Balance')
           print('5. Account details')
           choice_2 = int(input('your choice:'))
           if choice_2==1:
              deposit=int(input('How much money you want to deposit:'))
              print(acct_1.deposit(deposit))

           elif choice_2==2:
               withdraw = int(input('How much money you want to withdraw:'))
               print(acct_1.withdraw(withdraw))

           elif choice_2==3:
               print("Owner's name is:",end='')
               print(acct_1.owner)

           elif choice_2==4:
               print("Account Balance is:", end='')
               print(acct_1.balance)

           elif choice_2==5:
               print(acct_1)

           else:
               exit()

           print('\n')
           print('1.want to go back to the menu')
           print('2. Exit')
           choice_3 = int(input('Enter your choice:'))
           if choice_3 == 1:
               continue
           else:
               a,b = False

    else:
        a=False