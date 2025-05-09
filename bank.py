'''This mini banking app contains one admin, Admin username is admin and password admin123'''
'''I used function such as get_valid_amount(x),get_valid_amount(y) and get_valid_account_number() for input validation'''
'''I used files for store customers logins,customers details,account details,accounts transactions and accounts balances'''

#--------Input Validation-----------------

def get_valid_amount(x):
    while True:
        try:
            amount=float(input(f"Enter {x}:$"))
            if amount>0:
                return amount
            else:
                print("Enter positive number")
        except ValueError:
            print("Enter number only") 


def get_valid_name(y):
    while True:
       name=input(f"Enter {y}:")
       if name=="":
          print(f"{y} can not be empty")
       else:
          return name
 


def get_valid_account_number():
       name=input(f"Enter account number:")
       if name=="":
          print(f"account number can not be empty")
       else:
          return name
              


#----------Auto generate next id--------------------------


def get_next_user_id():
    
    try:
       with open("last_user_id.txt", "r") as file:
        last_id=file.read()
        
    except FileNotFoundError:
        last_id="u0" 

   
    number=int(last_id[1:]) + 1

   
    new_id="u" + str(number)

    with open("last_user_id.txt", "w") as file:
     file.write(new_id)   
    return new_id




def get_next_customer_id():
    
    try:
       with open("last_customer_id.txt", "r") as file:#read last customer id in last_customer_id.txt file
        last_id=file.read()                           #storing the customer id in the variable called last_id
        
    except FileNotFoundError:                         #this line work when first time login there is no file so FilenotFoundError comes in that that "c0" will assign to variable last_id
        last_id="c0"  

    
    number=int(last_id[1:]) + 1                       # last_id is string when we need to do calculations we need to slice the number part of id then make the number part into integer

   
    new_id="c" + str(number)                          #after add 1 with number part create new_id 

   
    with open("last_customer_id.txt", "w") as file:      #writing the id in last_customer_id.txt file
     file.write(new_id)   
    return new_id                                        


def get_next_account_number():
    
    try:
       with open("last_account_number.txt", "r") as file:
        last_account_number=file.read()
        
    except FileNotFoundError:
        last_account_number="1000"  

    
    last_account_number=int(last_account_number)+1

   
    new_account_number=str(last_account_number)

 
    with open("last_account_number.txt", "w") as file:
     file.write(new_account_number)   
    return new_account_number

#---------------Creating Customer----------------------------------

def create_customer():
   
   
   
   Customer_name=get_valid_name("customer's name")             #get input from user
   Customer_username=get_valid_name("username for customer")
   Customer_password=get_valid_name("user password")
   customer_id=get_next_customer_id()
   
   user_id=get_next_user_id()
   
   with open("customer_details.txt","a") as customer_details_file:                                    #storing user inputs in file
      customer_details_file.write(f"{customer_id},{Customer_name},{user_id},\n")
   with open("customer_login.txt","a") as customer_login_file:
      customer_login_file.write(f"{user_id},{customer_id},{Customer_username},{Customer_password},\n")
   print(f"User Created: ID:{user_id},Username:{Customer_username},Password:{Customer_password}")   
   print(f"Customer Created: ID:{customer_id},Name:{Customer_name}")   


#-----------------Creating Account-----------------------------

def create_account():
 
 
 customer_id=get_valid_name("customer id")
 pincode=get_valid_name("pincode for customer")
 try:
  with open("customer_details.txt","r") as customer_details_file:
    for line in customer_details_file:
       customer_details_list=line.split(",")
       if customer_details_list[0]==customer_id:
          Account_holder_name=customer_details_list[1]
          initial_balance=get_valid_amount("initial balance")
          Account_number=get_next_account_number()
          with open("accounts_details.txt","a") as accounts_details_file:
            accounts_details_file.write(f"{customer_id},{Account_number},{Account_holder_name},\n")
          with open("accounts_balance.txt","a") as accounts_balance_file:
            accounts_balance_file.write(f"{Account_number},{initial_balance},{pincode},\n")
          with open("accounts_transactions.txt","a") as accounts_transactions_file:
            accounts_transactions_file.write(f"{Account_number},Account created with balance {initial_balance},\n")
          
          print(f"Account created successfully! Your account number is {Account_number}.")
 except FileNotFoundError:
    print("customer id not found")






#-------------------Checking Balance-----------------------------------------

def check_balance_fun():
    Account_number=get_valid_account_number()
    Account_found=False
    try:
     with open("accounts_balance.txt","r") as accounts_balance_file:
       for line in accounts_balance_file:
          accounts_balance_list=line.split(",")
          if accounts_balance_list[0]==Account_number:
             Account_found=True
             Account_balance=accounts_balance_list[1]
                
             print(f"Account Number: {Account_number}")
             print(f"Current Balance: {Account_balance}")
             break
    except FileNotFoundError:
      pass

   
    if not(Account_found):
       print("Acccount not found") 


#----------------Deposit Function-------------------------------------------------------


def deposit_fun():
    Account_number=get_valid_account_number()
    Account_found=False
   
    
    try:
     with open("accounts_balance.txt","r") as accounts_balance_file:
       lines=accounts_balance_file.readlines()
       for index in range(len(lines)):
          line_list=lines[index].split(",")
          if line_list[0]==Account_number:
            Account_found=True
            amount=get_valid_amount("amount to deposit")
            Account_balance=float(line_list[1])
            Account_balance+=amount
            print(f"Amount {amount} deposited successfully! & Balance is {Account_balance} ")
            line_list[1]=Account_balance 
            lines[index]=f"{line_list[0]},{line_list[1]},{line_list[2]},\n"
    except FileNotFoundError:       
       pass
          
    
    if Account_found:
       with open("accounts_balance.txt","w") as accounts_balance_file:
             accounts_balance_file.writelines(lines)
       with open("accounts_transactions.txt","a") as accounts_transactions_file:
             accounts_transactions_file.write(f"{Account_number},Deposited amount {amount} & Balance is {Account_balance},\n")      
    else:  
       print("Account not found")

#----------------------Transaction Function--------------------------

def transaction_fun():
    Account_number=get_valid_account_number()
    Account_found=False

    try:
     with open("accounts_transactions.txt","r") as accounts_transactions_file:
       lines=accounts_transactions_file.readlines()
       
       print(f"Transaction History for Account {Account_number}:")
       for index in range(len(lines)):
          line_list=lines[index].split(",")
          if line_list[0]==Account_number:
            Account_found=True
            pincode_found=True
           
            print("-",line_list[1])

    except FileNotFoundError:
       pass

         
            
              
    if Account_found:
       pass
    else:
       print("Account not found")

#-------------------Creating menus for admin and customer--------------------------

def Admin_Menu():  
   print("\n====== ATM MENU ======")  
   print("1. Create Customer")   
   print("2. Create Account")   
   print("3. Check Balance") 
   print("4. Withdraw Money") 
   print("5. Deposit Money") 
   print("6. Transaction") 
   print("7. Exit")
  
def Customer_Menu():
   print("\n====== ATM MENU ======")     
   print("1. Check Balance") 
   print("2. Withdraw Money") 
   print("3. Deposit Money") 
   print("4. Transaction") 
   print("5. Exit")




#-------------------Withdraw Function-------------------------------------------------

def withdraw_function():
    Account_number=get_valid_account_number()
    pincode=get_valid_name("pincode")
    Account_found=False
    pincode_found=False
    try:
     with open("accounts_balance.txt","r") as accounts_balance_file: #open the accounts_balance.txt 
       lines=accounts_balance_file.readlines()                       #read all the lines in the file and store them as list of strings in variable lines 
       for index in range(len(lines)):                               #example:["1001,500.0,\n","1002,450.0,\n","1003,90.0,\n",....]
          line_list=lines[index].split(",")                          #split the current line into list using comma example ["1001","500.0","\n"]
          if line_list[0]==Account_number and line_list[2]==pincode: #checking the account number and pincode
            Account_found=True
            pincode_found=True                                       #if account found store True in Account_found
            Account_balance=float(line_list[1])                      #Convert line_list[1] from string to float for calculations
            amount=get_valid_amount("amount to withdraw")
            if amount<=Account_balance:
             Account_balance-=amount
             print(f"Amount {amount} withdrew successfully! Balance {Account_balance} ")
             line_list[1]=Account_balance                                                   #after doing calculations store the balance  in line_list[1]
             lines[index]=f"{line_list[0]},{line_list[1]},{line_list[2]},\n"                               #rebuild the line with changed balance
            else:
               print("Insufficient balance.")
    except FileNotFoundError:
       pass          
    
    if Account_found:
       if pincode_found:
         with open("accounts_balance.txt","w") as accounts_balance_file:                                                          #Open the "accounts_balance.txt" file in write mode
               accounts_balance_file.writelines(lines)                                                                            #write the updated lines in file
         with open("accounts_transactions.txt","a") as accounts_transactions_file:                                                #Open the "accounts_transactions.txt" file in append mode 
               accounts_transactions_file.write(f"{Account_number},Withdrew amount {amount} & Balance is {Account_balance},\n")   #write the transactions         
    else:  
       print("Incorrect account number or pincode")



def Admin():
 while True:   
   Admin_Menu()
   Choice=input("Enter the choice(1-7):") #Get the choice number from the user

   if Choice=="1":
      create_customer()
   elif Choice=="2":
      create_account() 
   elif Choice=="3":
      check_balance_fun() 
   elif Choice=="4":
      withdraw_function()
   elif Choice=="5":
      deposit_fun() 
   elif Choice=="6":
      transaction_fun()
   elif Choice=="7":
      print("Thanks for using our banking app")  
      exit() 
   else:
      print("Invalid input")   
     

def Customer():
 while True:   
   Customer_Menu()
   Choice=input("Enter the choice(1-5):")

   if Choice=="1":
      check_balance_fun() 
   elif Choice=="2":
      withdraw_function()
   elif Choice=="3":
      deposit_fun() 
   elif Choice=="4":
      transaction_fun()
   elif Choice=="5":
      print("Thanks for using our banking app")  
      exit() 
   else:
      print("Invalid input")   









def Main():
   while True:
    print("===Login===")
    user_name=get_valid_name("user name")
    user_password=get_valid_name("user password")
    if user_name=="admin" and user_password=="admin123": #this banking app has one admin 
        Admin()                                          #login to admin 
    else:
      try:
        with open("customer_login.txt","r") as customer_login_file: #opning customer_login.txt in reading mode
         for line in customer_login_file:                           #looping through each line in the file
          correct_password=line.split(",")                          #split the line using comma 
          if user_name==correct_password[2] and user_password==correct_password[3]: #checking username and password
             Customer()                                                             #login to customer 
         print("incorrect username or password")
      except FileNotFoundError:                                                     #this will work when there is file not found when admin input wrong user name or password
         print("Retry")



Main()
