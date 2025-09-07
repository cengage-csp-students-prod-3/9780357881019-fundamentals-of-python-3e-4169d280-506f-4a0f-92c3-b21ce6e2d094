## Instructions

The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%. Monthly payments are 5% of the listed purchase price.

Write a program in the file **tidbit.py** that takes the purchase price as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain the following items:

- the month number (beginning with 1)
- the current total balance owed
- the interest owed for that month
- the amount of principal owed for that month
- the payment for that month
- the balance remaining after payment

The amount of interest for a month is equal to balance \* rate / 12. The amount of principal for a month is equal to the monthly payment minus the interest owed. (LO: 3.2, 3.3, 3.4)

An example of the program is shown below:

```txt
Enter the purchase price: 200
Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance
 1         180.00           1.80             8.20            10.00           170.00
 2         170.00           1.70             8.30            10.00           160.00
 3         160.00           1.60             8.40            10.00           150.00
 4         150.00           1.50             8.50            10.00           140.00
 5         140.00           1.40             8.60            10.00           130.00
 6         130.00           1.30             8.70            10.00           120.00
 7         120.00           1.20             8.80            10.00           110.00
 8         110.00           1.10             8.90            10.00           100.00
 9         100.00           1.00             9.00            10.00            90.00
10          90.00           0.90             9.10            10.00            80.00
11          80.00           0.80             9.20            10.00            70.00
12          70.00           0.70             9.30            10.00            60.00
13          60.00           0.60             9.40            10.00            50.00
14          50.00           0.50             9.50            10.00            40.00
15          40.00           0.40             9.60            10.00            30.00
16          30.00           0.30             9.70            10.00            20.00
17          20.00           0.20             9.80            10.00            10.00
18          10.00           0.10             9.90            10.00             0.00
```

## Your Tasks
