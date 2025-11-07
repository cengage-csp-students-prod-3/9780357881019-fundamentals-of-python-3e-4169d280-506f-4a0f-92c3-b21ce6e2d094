# doctor_model.py
import random

class Doctor:
    """Represents a simple conversational doctor."""

    def __init__(self):
        # Some possible generic responses
        self.responses = [
            "You seem to think that {0}?",
            "Did I just hear you say that {0}?",
            "Why do you believe that {0}?",
            "I would like to hear more about that.",
            "And what do you think about this?",
            "Go on."
        ]

    def greeting(self):
        """Return a greeting message."""
        return "Hello, how can I help you today?"

    def farewell(self):
        """Return a farewell message."""
        return "Have a nice day!"

    def reply(self, user_input):
        """Return a randomized reply string."""
        # Choose a random response template
        response = random.choice(self.responses)

        # Fill in the template if it includes a placeholder
        if "{0}" in response:
            return response.format(user_input)
        else:
            return response
