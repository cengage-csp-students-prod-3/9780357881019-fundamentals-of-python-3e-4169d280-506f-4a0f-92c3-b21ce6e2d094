# Write your program here

numbers = []

while True:
    userInput = input("Enter a number or press Enter to quit:")
    
    if userInput == "":
        break 
    
    try:
        number = float(userInput)  
        numbers.append(number)      
    except ValueError:
        print("Invalid input. Please enter a number.")

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"\nThe sum is {total}")
    print(f"The average is {average}")
else:
    print("\nNo numbers were entered.")