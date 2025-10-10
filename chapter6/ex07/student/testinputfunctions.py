# Write your code here
def inputFloat(prompt="Please enter an integer or a float: "):
    """Prompt the user for a float value, validating the input."""
    while True:
        user_input = input(prompt).strip()

        # Count number of decimal points
        if user_input.count('.') > 1:
            print("Error: the input cannot have more than one '.'")
            continue

        # Check that all characters are digits or a single '.'
        allowed_chars = set("0123456789.")
        if not set(user_input).issubset(allowed_chars):
            print("Error: the input must consist only of digits")
            continue

        # Handle empty input or single '.'
        if user_input == "" or user_input == ".":
            print("Error: please enter a valid number")
            continue

        # Convert to float and return
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Error: please enter a valid number")


# Test the function
if __name__ == "__main__":
    result = inputFloat()
    print(result)