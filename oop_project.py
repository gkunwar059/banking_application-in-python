from bank_account import *

Ganesh =BankAccount(1000,"Ganesh Kunwar")

 
Susma=BankAccount(2000,"Susma Bhandari")

# to get the balance of Susma bhandari & Ganesh Kunwar
Susma.getBalance()
Ganesh.getBalance()


# deposted money 
Susma.getDeposit(2000)
Ganesh.getDeposit(4000)

# withdraw the balance:
Susma.withdraw(100)
Ganesh.withdraw(200)

# transfer the balance
Susma.transfer(100,Ganesh)
Ganesh.transfer(4,Susma)

Laxmi=InterestRewardsAct(1000,"Laxmi")

Laxmi.getBalance()
Laxmi.deposit(1000)
Laxmi.transfer(100,Susma)


# Saving Account :

Nitesh=SavingAcct(1000,"Nitesh")
Nitesh.getBalance()
Nitesh.deposit(100)
Nitesh.transfer(100,Susma)
