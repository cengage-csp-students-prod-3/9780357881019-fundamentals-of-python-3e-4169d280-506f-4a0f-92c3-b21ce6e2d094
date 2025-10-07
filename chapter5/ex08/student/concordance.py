# Write your program here
import re
from collections import defaultdict

def clean_word(word):
    """Remove punctuation and convert to lowercase."""
    return re.sub(r'[^\w\s]', '', word).lower()

def get_words_from_file(filename):
    """Read file and return a list of cleaned words."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content.lower())  # Find words
        return words

def build_concordance(words, n=1):
    """Build concordance dictionary for n-word sequences."""
    concordance = defaultdict(int)

    if len(words) < n:
        return concordance

    for i in range(len(words) - n + 1):
        seq = ' '.join(words[i:i+n])
        concordance[seq] += 1

    return concordance

def main():
    filename = input("Enter the input file name: ")
    try:
        words = get_words_from_file(filename)

        # Ask for n (how many words in a sequence)
        n_input = input("Enter the number of words per sequence (default is 1): ").strip()
        n = int(n_input) if n_input else 1

        concordance = build_concordance(words, n)

        for word_seq in sorted(concordance):
            print(f"{word_seq} {concordance[word_seq]}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()