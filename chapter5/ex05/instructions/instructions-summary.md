## Instructions

Chapter 4 presented an algorithm for converting from binary to decimal. You can generalize this algorithm to work for a representation in any base. Instead of using a power of 2, this time you use a power of the base. Also, you use digits greater than 9, such as A … F, when they occur.

Define a function named `repToDecimal` in the file **convert.py** that expects two arguments, a string and an integer. The second argument should be the base. For example, `repToDecimal("10", 8)` returns 8, whereas `repToDecimal("10", 16)` returns 16. The function should use a lookup table to find the value of any digit. Make sure that this table (it is actually a dictionary) is initialized before the function is defined. For its keys, use the 10 decimal digits (all strings) and the letters A … F (all uppercase). The value stored with each key should be the integer that the digit represents. (The letter 'A' associates with the integer value 10, and so on.) The main loop of the function should convert each digit to uppercase, look up its value in the table, and use this value in the computation. Include a `main` function that tests the conversion function with numbers in several bases. (LO: 5.2, 5.3)

<!--There is no helpful example output for this exercise-->

## Your Tasks
