import re
import sys
from collections import defaultdict

def get_words_from_file(filename):
    """Read file and return list of lowercase words."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content.lower())
        return words

def build_concordance(words, n=1):
    """Build concordance dictionary for n-word sequences."""
    concordance = defaultdict(int)
    for i in range(len(words) - n + 1):
        seq = ' '.join(words[i:i+n])
        concordance[seq] += 1
    return concordance

def main():
    try:
        # Try to get arguments from command-line first
        if len(sys.argv) >= 2:
            filename = sys.argv[1]
        else:
            filename = input("Enter the input file name: ")

        if len(sys.argv) >= 3:
            n = int(sys.argv[2])
        else:
            n_input = input("Enter the number of words per sequence (default is 1): ").strip()
            n = int(n_input) if n_input else 1

        words = get_words_from_file(filename)
        concordance = build_concordance(words, n)

        for word_seq in sorted(concordance):
            print(word_seq)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Please enter a valid number for n.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()