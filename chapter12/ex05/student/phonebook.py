# Write your code here
# File: phonebook.py

import os
import json

class PhoneBook:
    """Represents a shared phone book stored in a file."""

    def __init__(self, filename="phonebook_data.json"):
        self.filename = filename
        self.load()

    def load(self):
        """Loads existing phonebook data from file or initializes an empty book."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.book = json.load(f)
        else:
            self.book = {}

    def save(self):
        """Saves current phonebook data to file."""
        with open(self.filename, "w") as f:
            json.dump(self.book, f)

    def lookup(self, name):
        """Returns the number for a given name or None if not found."""
        return self.book.get(name)

    def add(self, name, number):
        """Adds or updates a name-number pair in the phone book."""
        self.book[name] = number
        self.save()
