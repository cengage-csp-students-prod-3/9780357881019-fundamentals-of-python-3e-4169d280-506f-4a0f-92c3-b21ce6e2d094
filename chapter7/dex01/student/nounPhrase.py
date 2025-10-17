import random

articles = ["the", "a", "one", "some", "any"]
adjectives = ["big", "small", "blue", "green", "yellow", "red", "purple", "orange", "brown", "black", "white"]
nouns = ["apple", "peach", "banana", "pear", "orange", "grape", "strawberry", "blueberry", "raspberry", "cherry", "watermelon", "cantaloupe", "honeydew"]

# nounphrase = article [adjectivephrase] noun
def nounPhrase():
    """Builds and returns a noun phrase."""
    phrase = random.choice(articles) + " "
    # Randomly decide whether to include adjectives
    if random.choice([True, False]):
        phrase += adjectivePhrase() + " "
    phrase += random.choice(nouns)
    return phrase

# adjectivephrase = adjective [adjectivephrase]
def adjectivePhrase():
    """Builds and returns an adjective phrase."""
    phrase = random.choice(adjectives)
    # Randomly decide whether to continue adding adjectives
    if random.choice([True, False]):
        phrase += " " + adjectivePhrase()
    return phrase

print(nounPhrase())