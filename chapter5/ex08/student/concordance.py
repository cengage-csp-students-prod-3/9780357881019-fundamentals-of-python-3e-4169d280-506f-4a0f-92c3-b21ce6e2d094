import sys
import re
from collections import defaultdict

def get_words(filename):
    """Read file and return list of lowercase words."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
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
        # Prefer command-line args
        if len(sys.argv) >= 2:
            filename = sys.argv[1]
        else:
            # Fall back to input() only if in terminal
            filename = input("Enter the input file name: ").strip()

        if len(sys.argv) >= 3:
            n = int(sys.argv[2])
        else:
            n_input = input("Enter the number of words per sequence (default is 1): ").strip()
            n = int(n_input) if n_input else 1

        words = get_words(filename)
        concordance = build_concordance(words, n)

        for phrase in sorted(concordance):
            print(' '.join(word.capitalize() for word in phrase.split()))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()