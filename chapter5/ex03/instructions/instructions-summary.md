## Instructions

Modify the sentence-generator program of _Case Study 5-1_ (in the file **generator.py**) so that it inputs its vocabulary from a set of text files at startup. The filenames are **nouns.txt**, **verbs.txt**, **articles.txt**, and **prepositions.txt**. (Hint: Define a single new function, `getWords`. This function should expect a filename as an argument. The function should open an input file with this name, define a temporary list, read words from the file, and add them to the list. The function should then convert the list to a tuple and return this tuple. Call the function with an actual filename to initialize each of the four variables for the vocabulary.) (LO: 5.1, 5.2)

An example of the program is shown below:

```
Enter the number of sentences: 2
A BAT LIKED A GIRL BY A BALL
A BOY SAW THE BAT WITH THE GIRL
```

## Your Tasks
