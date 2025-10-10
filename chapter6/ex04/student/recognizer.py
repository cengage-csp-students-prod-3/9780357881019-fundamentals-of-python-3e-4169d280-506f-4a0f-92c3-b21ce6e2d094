# Write your code here
articles = {"the", "a", "an"}
nouns = {"boy", "girl", "ball", "bat"}
verbs = {"hit", "saw"}
prepositions = {"with"}
adjectives = {"red", "big", "small"}         # NEW: adjectives
conjunctions = {"and", "but"}                # NEW: conjunctions

def sentence(words):
    """Recognize a complete sentence."""
    success, remainder = simple_sentence(words)
    if success and remainder == []:
        return True, remainder
    # NEW: handle compound sentences joined by a conjunction
    if success and remainder and remainder[0] in conjunctions:
        success2, remainder2 = simple_sentence(remainder[1:])
        if success2 and remainder2 == []:
            return True, remainder2
    return False, words


def simple_sentence(words):
    """Recognize a single independent clause (no conjunctions)."""
    success, remainder = noun_phrase(words)
    if success:
        success2, remainder2 = verb_phrase(remainder)
        if success2:
            return True, remainder2
    return False, words


def noun_phrase(words):
    """Recognize noun phrases like 'the girl' or 'the red ball'."""
    if words and words[0] in articles:
        words = words[1:]
        # Optionally include adjective
        if words and words[0] in adjectives:
            words = words[1:]
        if words and words[0] in nouns:
            return True, words[1:]
    return False, words


def verb_phrase(words):
    """Recognize verb phrases with optional prepositional phrase."""
    if words and words[0] in verbs:
        words = words[1:]
        success, remainder = noun_phrase(words)
        if success:
            # Verb phrase can optionally have a prepositional phrase
            if remainder and remainder[0] in prepositions:
                success2, remainder2 = prepositional_phrase(remainder)
                if success2:
                    return True, remainder2
            # NEW: allow verb phrase without prepositional phrase
            return True, remainder
    return False, words


def prepositional_phrase(words):
    """Recognize 'with a bat', etc."""
    if words and words[0] in prepositions:
        success, remainder = noun_phrase(words[1:])
        if success:
            return True, remainder
    return False, words


def main():
    while True:
        sentence_input = input("Enter a sentence or press return to quit: ").lower().strip()
        if sentence_input == "":
            break
        words = sentence_input.split()
        ok, _ = sentence(words)
        if ok:
            print("Ok, grammatically correct")
        else:
            print("Not grammatically correct")


if __name__ == "__main__":
    main()