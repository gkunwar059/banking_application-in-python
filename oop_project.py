from bank_account import *
# # bank account 
# Ganesh =BankAccount(1000,"Ganesh Kunwar")
# Susma=BankAccount(2000,"Susma Bhandari")

# # to get the balance of Susma bhandari & Ganesh Kunwar
# Susma.getBalance()
# Ganesh.getBalance()


# # deposted money 
# Susma.getDeposit(2000)
# Ganesh.getDeposit(4000)

# # withdraw the balance:
# Susma.withdraw(100)
# Ganesh.withdraw(200)

# # transfer the balance
# Susma.transfer(100,Ganesh)
# Ganesh.transfer(4,Susma)

# Laxmi=InterestRewardsAct(1000,"Laxmi")

# Laxmi.getBalance()
# Laxmi.deposit(1000)
# Laxmi.transfer(100,Susma)


# # Saving Account :

# Nitesh=SavingAcct(1000,"Nitesh")
# Nitesh.getBalance()
# Nitesh.deposit(100)
# Nitesh.transfer(100,Susma)


initial_amount=float(input("Enter the initial amount for the bank account :"))
account_name=input("Enter the account name:")
user_account=SavingAcct(initial_amount,account_name)



# perform the operation based on user input :
while True:
    print("\nOptions:")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Transfer")
    print("4.Get Balance")
    print("5.Quit")
    
    choice=input( "Enter the choice (1-5)")
    
    if choice=='1':
        deposit_amount=float(input("Enter the deposit amount:"))
        user_account.getDeposit(deposit_amount)
    elif choice=='2':
        withdraw_amount=float(input("enter the withdraw amount :"))
        user_account.withdraw(withdraw_amount)
        
    elif choice=='3':
        transfer_amount=float(input("Enter the transfer amount :"))
        target_account_name=input("Enter the target account name :")
        target_account=SavingAcct(0,target_account_name)
        user_account.transfer(transfer_amount,target_account)    

    elif choice=='4':
        user_account.getBalance()
        
    elif choice=='5':
        print("Existing Program ")
        break
    else:
        print("Invalid choice . Please enter a number between 1 and 5 .")




























# def create_bank_account_from_user_input():
#     name=input("Enter the name :")
#     initial_amount=float(input("Enter the initial amount :"))
#     account_type=input("Enter account type (1-Bank Account ,2-Interest Rewards Account ,3-Saving Account :")

#     if account_type==1:
#         return BankAccount(initial_amount,name)
    
#     elif account_type==2:
#         return InterestRewardsAct(initial_amount,name)
    
#     elif account_type==3:
#         return SavingAcct(initial_amount,name)
    
#     else:
#         print("invalid account type.Creating Bank Account .")
#         return BankAccount(initial_amount,name)
    
# create_bank_account_from_user_input()
    