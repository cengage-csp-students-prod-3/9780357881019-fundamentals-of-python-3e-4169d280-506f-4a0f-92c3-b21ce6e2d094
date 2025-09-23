from decimal import Decimal, ROUND_HALF_DOWN

purchase_price = Decimal(input("Enter the purchase price: ").strip())

down_payment_rate = Decimal('0.10')
annual_interest_rate = Decimal('0.12')
monthly_rate = annual_interest_rate / Decimal('12')

monthly_payment = (purchase_price * Decimal('0.05')).quantize(Decimal('0.01'), rounding=ROUND_HALF_DOWN)
balance = (purchase_price * (Decimal('1') - down_payment_rate)).quantize(Decimal('0.01'), rounding=ROUND_HALF_DOWN)

print("Month  Starting Balance. Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1
while balance > 0:
    start = balance
    payment = monthly_payment

    start_has_cents = (start % 1) !=0
    
    if start <= payment and start_has_cents:
        monthly_interest = Decimal('0.00')
    else:
        monthly_interest = (start * monthly_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_DOWN)
    
    principal = (payment - monthly_interest).quantize(Decimal('0.01'), rounding=ROUND_HALF_DOWN)

    remaining_balance = (start - payment).quantize(Decimal('0.01'), rounding=ROUND_HALF_DOWN)
    if remaining_balance < 0:
        remaining_balance = Decimal('0.00')

    print(f"{month:>2}{start:>17.2f}{monthly_interest:>17.2f}"
          f"{principal:>18.2f}{payment:>10.2f}{remaining_balance:>15.2f}")
    
    balance = remaining_balance
    month += 1