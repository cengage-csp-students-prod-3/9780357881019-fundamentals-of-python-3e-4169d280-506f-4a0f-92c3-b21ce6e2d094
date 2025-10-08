import random

hedges = (
    "Please tell me more.",
    "Many of my patients tell me the same thing.",
    "Please continue."
)

qualifiers = (
    "Why do you say that ",
    "You seem to think that ",
    "Can you explain why "
)

# ✅ Expanded replacement dictionary (two-way reflection)
replacements = {
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "me": "you",
    "mine": "yours",
    "you": "I",
    "you'd": "I would",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "am": "are",
    "are": "am"
}

def reply(sentence):
    """Implements two different reply strategies."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
    """Replaces first and second person pronouns appropriately."""
    words = sentence.lower().split()
    replyWords = []
    for word in words:
        # Replace word if found, otherwise keep as is
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()