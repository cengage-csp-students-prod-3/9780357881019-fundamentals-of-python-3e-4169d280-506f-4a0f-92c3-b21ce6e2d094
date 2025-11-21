"""
File: doctorclienthandler.py

Handles persistent doctor sessions by patient name.
"""

import os
import pickle
from threading import Thread
from codecs import decode, encode
from doctor import Doctor   # Import your Doctor class

class DoctorClientHandler(Thread):

    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        self.doctor = None
        self.patient_name = None

    def run(self):
        try:
            # Step 1: Receive patient name
            self.patient_name = decode(self.client.recv(1024), "ascii").strip()

            # Step 2: Check for existing file
            filename = f"{self.patient_name}.dat"

            if os.path.exists(filename):
                # Load existing patient history
                with open(filename, "rb") as file:
                    self.doctor = pickle.load(file)
                self.client.send(encode(f"Welcome back, {self.patient_name}! How are you feeling today?\n", "ascii"))
            else:
                # New patient
                self.doctor = Doctor(self.patient_name)
                self.client.send(encode(f"Hello {self.patient_name}, I'm Dr. AI. What brings you in today?\n", "ascii"))

            # Step 3: Conversation loop
            while True:
                message = decode(self.client.recv(1024), "ascii").strip()

                if not message or message.lower() == "quit":
                    break

                response = self.doctor.reply(message)
                self.client.send(encode(response + "\n", "ascii"))

        finally:
            # Step 4: Save patient history when done
            with open(f"{self.patient_name}.dat", "wb") as file:
                pickle.dump(self.doctor, file)

            self.client.close()
