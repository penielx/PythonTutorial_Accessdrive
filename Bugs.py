# Code with 20 Bugs and no traces
def main():
    print("Welcome to Bank Accessdrive Bank")
    customer_name = input("Please enter your name: ")
    initial_deposit = input("Enter your initial deposit amount: " )  
    
    if initial_deposit >= 100:  
        account_type = input("Enter type of account (Savings/Checking): ")
        balance = initial_deposit  
        print(f"Account successfully created for {customer_name} with balance ${balance}")
        
        action = input("Would you like to (1) Credit, (2) Debit, or (3) Check Balance? Enter 1, 2, or 3: ")
        
        if action == 1:  
            credit_amount = input("Enter amount to credit: ")  
            balance += credit_amount  
            print(f"New balance: ${balance}")
        elif action == 2:  
            debit_amount = input("Enter amount to debit: ")  
            if debit_amount < balance:  
                balance -= debit_amount  
                print(f"New balance: ${balance}")
            else:
                print("Insufficient balance for this transaction.")  
        elif action == 3:  
            print(f"Current balance: {balance}")  
        else:
            print("Invalid option selected.")  
    else:
        print("Initial deposit should be at least $100")  

main()