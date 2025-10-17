# Write your code here
def main():
    # Ask the user for the input file name
    filename = input("Enter the input file name: ")

    # Open the file and read its contents
    with open(filename, "r") as file:
        # Read all numbers from the file as strings, split by whitespace
        numbers = file.read().split()

    # Convert strings to floats using map (higher-order function #1)
    numbers = list(map(float, numbers))

    # Compute the average using sum (higher-order function #2)
    average = sum(numbers) / len(numbers)

    # Print the result
    print(f"The average is {average}")

# Run the program
if __name__ == "__main__":
    main()