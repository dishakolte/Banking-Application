#Banking Application

accountNo = 0
customerName = " "
branchCode = " "
mobileNo = 0
balance = 0

def createAccount():
    accountNo = int(input("Enter Account Number:"))
    customerName = input("Enter Customer Name:")
    branchCode = input("Enter Branch Code:")
    mobileNo = int(input("Enter Mobile Number:"))
    balance = int(input("Enter Current Balance"))
    
def showAccountDetails():
    print("Account Number:",accountNo)
    print("Customer Name:",customerName)
    print("Branch Code:",branchCode)
    print("Mobile Number:",mobileNo)
    
def depositAccount(amount):
    balance = balance+amount
    checkBalance()
    
def withdrawAccount(amount):
    balance = balance-amount
    checkBalance()
    
def showBalance():
    print("Current Balance:",balance)
    
#_Main_#

print("----------Welcome to the Banking Application!!----------")
print(" 1.Create Account \n 2.Deposit Account \n 3.Withdraw Account \n 4.Show Balance \n")
ch = int(input("Select your choice: \n"))
if(ch==1):
    createAccount()
elif(ch==2):
    amount=int(input("Enter amount to deposit"))
    depositAccount(amount)
elif(ch==3):
    amount=int(input("Enter amount to withdraw"))
    withdrawAccount(amount)
elif(ch==4):
    checkBalance()
else:
    print("Invalid Choice")
    
    