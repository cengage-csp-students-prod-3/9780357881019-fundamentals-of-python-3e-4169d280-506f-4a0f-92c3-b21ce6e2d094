purchase_price = float(input("Enter the purchase price: "))

down_payment = purchase_price * 0.10
balance = purchase_price - down_payment

monthly_payment = purchase_price * 0.05

monthly_interest_rate = 0.12 / 12

print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1

while balance > 0.005:  
    interest = round(balance * monthly_interest_rate, 2)
    principal = round(monthly_payment - interest, 2)
    ending_balance = round(balance - principal, 2)

    if ending_balance < 0:
        principal += ending_balance  
        ending_balance = 0.00

    print(f"{month:<6} {balance:>16.2f} {interest:>16.2f} {principal:>17.2f} {monthly_payment:>8.2f} {ending_balance:>15.2f}")

    balance = ending_balance
    month += 1