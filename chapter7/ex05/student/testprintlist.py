# Write your code here
def printAll(seq):
    """Recursively prints all elements of a sequence and traces each call."""
    print(f"Calling printAll({seq})")  # Trace statement to show the current argument
    if seq:  # Base case: if the sequence is not empty
        print(seq[0])  # Print the first element
        printAll(seq[1:])  # Recursive call with the rest of the sequence

# --- Test code ---
if __name__ == "__main__":
    # Example tests
    print("Testing with a list:")
    printAll([1, 2, 3, 4])

    print("\nTesting with a string:")
    printAll("HELLO")

    print("\nTesting with a tuple:")
    printAll((10, 20, 30))