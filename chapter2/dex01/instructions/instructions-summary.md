## Instructions

Jill has written a program that computes the sales tax on the purchase of an item, given the price of the item (a floating-point number) and the percent tax rate (an integer). The output of the program is the purchase price, the tax, and the total amount to be paid. Here is her code:

```python
purchasePrice = float(input("Enter the purchase price as $: "))
taxRate = int(input("Enter the tax rate as %: "))
tax = purchasePrice * taxRate
totalOwed = purchasePrice + tax
print("Purchase price: ", purchasePrice)
print("Tax: ", tax)
print("Total owed: ", totalOwed)
```

When she tested his program with a purchase price of $5.50 and a sales tax of 5%, Jill observed the following unexpected output:

```txt
Enter the purchase price as $: 5.50
Enter the tax rate as %: 5
Purchase price: 5.5
Tax: 27.5
Total owed: 33.0
```

Determine what causes this error and fix it.

## Your Tasks
