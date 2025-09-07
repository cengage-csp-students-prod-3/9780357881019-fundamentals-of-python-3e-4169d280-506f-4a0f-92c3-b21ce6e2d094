## Instructions

Jill points out to Jack that English grammar allows a noun to be modified by zero or more adjectives. Examples are “The girl hit the ball,” “The girl hit the red ball,” and “The girl hit the little red ball.” She asks Jack to design and implement a function to generate noun phrases based on the following grammar rules:

```
nounphrase = article [adjectivephrase] noun
adjectivephrase = adjective [adjectivephrase]
```

where an adjective phrase is one or more adjectives (remember that the`[]` brackets indicate an optional item in a grammar rule). Jack’s code for the `nounPhrase` and `adjectivePhrase` functions follows:

```python
#nounphrase = article [adjectivephrase] noun
def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + \
        adjectivePhrase() + " " + random.choice(nouns)

#adjectivephrase = adjective [adjectivephrase]
def adjectivePhrase():
    """Builds and returns an adjective phrase."""
    return random.choice(adjectives) + " " + adjectivePhrase()
```

When Jack tests the `nounPhrase` function, the PVM halts the program with a `RecursionError`. Determine why this error occurs and correct it.

## Your Tasks
