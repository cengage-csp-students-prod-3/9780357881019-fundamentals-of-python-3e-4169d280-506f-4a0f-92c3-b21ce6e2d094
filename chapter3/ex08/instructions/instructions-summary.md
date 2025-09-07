## Instructions

The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided into both of them. Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive integers. You can implement this algorithm in the following manner:

1.  Compute the remainder of dividing the larger number by the smaller number.
1.  Replace the larger number with the smaller number and the smaller number with the remainder.
1.  Repeat this process until the smaller number is zero.
1.  The larger number at this point is the GCD of A and B.

Write a program in the file **gcd.py** that lets the user enter two integers and then prints each step in the process of using the Euclidean algorithm to find their GCD. (LO: 3.4)

An example of the program is shown below:

```txt
Enter the smaller number: 5
Enter the larger number: 15

The greatest common divisor is 5
```

## Your Tasks
