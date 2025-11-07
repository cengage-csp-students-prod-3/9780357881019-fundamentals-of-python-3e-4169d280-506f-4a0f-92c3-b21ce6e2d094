# Write your code here
# doctor.py
from doctor_model import Doctor

def main():
    """Main function for user interaction with the Doctor."""
    doc = Doctor()
    print(doc.greeting())

    while True:
        user_input = input("> ")

        if user_input.lower() == "quit":
            print(doc.farewell())
            break
        else:
            print(doc.reply(user_input))

if __name__ == "__main__":
    main()
