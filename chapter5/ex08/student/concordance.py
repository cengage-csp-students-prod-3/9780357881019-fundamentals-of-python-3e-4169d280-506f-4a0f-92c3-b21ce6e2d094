import sys
import re
from collections import defaultdict

def get_words(filename):
    """Read file and return list of lowercase words with punctuation removed."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        words = re.findall(r'\b\w+\b', content.lower())
        return words

def build_concordance(words, n=1):
    """Return a dictionary of n-word sequences and their frequencies."""
    concordance = defaultdict(int)
    for i in range(len(words) - n + 1):
        phrase = ' '.join(words[i:i+n])
        concordance[phrase] += 1
    return concordance

def main():
    if len(sys.argv) < 2:
        print("Error: Missing input file name.")
        return

    filename = sys.argv[1]
    try:
        n = int(sys.argv[2]) if len(sys.argv) >= 3 else 1
    except ValueError:
        print("Error: Invalid value for n.")
        return

    try:
        words = get_words(filename)
        concordance = build_concordance(words, n)

        for phrase in sorted(concordance):
            print(f"{phrase} {concordance[phrase]}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()