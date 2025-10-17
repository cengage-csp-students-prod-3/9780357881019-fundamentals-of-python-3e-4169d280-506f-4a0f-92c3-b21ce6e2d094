def printAll(seq):
    """Recursively prints the sequence, shorter each time."""
    if seq:
        print(seq)       # Print the current (remaining) sequence
        printAll(seq[1:])  # Recursive call with a shorter slice

# --- Test code ---
if __name__ == "__main__":
    print("Testing with a list:")
    printAll([1, 2, 3, 4])