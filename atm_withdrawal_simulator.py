#Set a fixed variable representing a bank balance
balance = 500

#Prompt user to withdraw
withdrawal = int(input("How much would you like to withdraw? "))

#Handle negative or zero input
if withdrawal <= 0:
    print("Invalid amount. You must withdraw more than R0")

elif withdrawal <= balance:
    balance -= withdrawal
    print(F"Withdrawal successful! Remaining balance: R{balance}")

else:
    print("Declined. Insufficient funds!")