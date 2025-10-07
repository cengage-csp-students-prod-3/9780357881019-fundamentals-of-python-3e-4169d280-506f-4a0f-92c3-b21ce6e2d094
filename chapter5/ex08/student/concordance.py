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
    try:
        filename = input("Enter the input file name: ").strip()
        n_input = input("Enter the number of words per sequence (default is 1): ").strip()
        n = int(n_input) if n_input else 1

        words = get_words(filename)
        concordance = build_concordance(words, n)

        for phrase in sorted(concordance):
            print(f"{phrase} {concordance[phrase]}")

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid number entered for sequence length.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()