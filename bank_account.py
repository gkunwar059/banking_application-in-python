#  SOURCE VIDEO:# https://www.youtube.com/watch?v=PMFd95RgIwE&t=3s
class BankException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_amount,account_name):
        self.balance=initial_amount
        self.name=account_name
        print(f"\n Account '{self.name}' created .\nBalance =${self.balance:.2f} ")  
        
        
    # get balance 
    def getBalance(self):
        print(f"\n  Account '{self.name}={self.balance}'   ")  
        
        
    def getDeposit(self,amount):
        self.balance=self.balance+amount
        print(f"\n Deposit Complete Account '{self.name} deposited  {self.balance}'")
        self.getBalance()
 
    def viableTrasction(self,amount):
        ''' This is implemented to check the account has a balance or not ? 
        
        '''
        if self.balance >= amount:
            return True
        else:
            raise BankException(f"\n  Sorry , account '{self.name}' only has a balance ${self.balance:.2f}")
        
        
    def withdraw(self,amount):
        try:
            self.viableTrasction(amount)
            self.balance=self.balance-amount
            print("\n Withdraw Complete !! ")
            self.getBalance()
            
        except BankException as error:
              print(f'\n Withdraw  interrupted:{error} ')     
              
              
    def transfer(self,amount,account):
        try:
            print("\n **************** \n \n Beginning Transfer .... ")  
            self.viableTrasction(amount)
            self.viableTrasction(amount)
            self.withdraw(amount)
            account.getDeposit(amount)
            print('\n Transfer Complete ! \n \n ***************')
        except BankException as error:
            print(f'\n Transfer interrupted . X{error}')    
        
class InterestRewardsAct(BankAccount):
    def deposit(self,amount):
        self.balance=self.balance+(amount * 1.05)
        print("\n Deposit Complete ...")
        self.getBalance()
        
    
class SavingAcct(InterestRewardsAct):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount,account_name)
        self.fee=5
        
    def withdraw(self, amount):
        try:
            self.viableTrasction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\n Withdraw Complete ....")
            self.getBalance()
        except BankException as error:
            print(f"\n Withdraw interrupted :{error}")