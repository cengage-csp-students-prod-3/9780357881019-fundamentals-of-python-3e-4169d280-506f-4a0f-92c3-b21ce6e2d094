"""
File: salestax.py
Inputs: The purchase price of an item and the tax rate as an integer percent
Outputs: The purchase price, the tax computed, and the total amount to be paid
"""

purchasePrice = float(input("Enter the purchase price as $: "))
taxRate = int(input("Enter the tax rate as %: "))
tax = purchasePrice * taxRate
totalOwed = purchasePrice + tax
print("Purchase price: ", purchasePrice)
print("Tax:            ", tax)
print("Total owed:     ", totalOwed)