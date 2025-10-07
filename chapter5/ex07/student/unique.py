# Write your program here
def main():
    # Prompt user for input file
    filename = input("Enter the input file name: ")

    try:
        with open(filename, 'r') as file:
            text = file.read()

        # Split into words
        words = text.split()

        # Strip punctuation but keep original casing
        cleaned_words = [word.strip('.,!?()[]{}:;"\'') for word in words]

        # Get unique words (case-sensitive)
        unique_words = sorted(set(cleaned_words))

        # Print each word on its own line
        for word in unique_words:
            print(word)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()