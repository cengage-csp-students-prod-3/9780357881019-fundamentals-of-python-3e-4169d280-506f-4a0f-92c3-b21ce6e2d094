import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacements = {"I": "you", "me": "you", "my": "your",
                "we": "you", "us": "you", "mine": "yours",
                "am": "are", "you": "I", "your": "my"} 


def changePerson(sentence):
    """Replaces first-person pronouns with second-person pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        # Handle punctuation separately if needed
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)


def reply(sentence):
    """Implements two different reply strategies."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)


def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")

    history = []       # Store previous patient inputs
    exchange_count = 0 # Track number of turns

    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break

        history.append(sentence)
        exchange_count += 1

        # --- Recall earlier topic occasionally after several exchanges ---
        if exchange_count > 4 and random.random() < 0.25:
            past_sentence = random.choice(history[:-1])  # pick earlier statement
            recalled = changePerson(past_sentence)
            print("Earlier you said that " + recalled)
        else:
            print(reply(sentence))


# The entry point for program execution
if __name__ == "__main__":
    main()