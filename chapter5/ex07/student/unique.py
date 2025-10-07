# Write your program here
def main():
    # Prompt for input file name
    filename = input("Enter the input file name: ")

    try:
        # Open and read the file
        with open(filename, 'r') as file:
            text = file.read()

        # Split text into words
        words = text.split()

        # Normalize words (remove punctuation and convert to lowercase)
        cleaned_words = [word.strip('.,!?()[]{}:;"\'').lower() for word in words]

        # Get unique words using a set
        unique_words = sorted(set(cleaned_words))

        # Print the unique words
        for word in unique_words:
            print(word)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()