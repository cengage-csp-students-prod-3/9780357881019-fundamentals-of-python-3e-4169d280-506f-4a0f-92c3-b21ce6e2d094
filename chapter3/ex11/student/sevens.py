# Write your program here
import random

# Get starting money from the user
money = int(input("How many dollars do you have? "))

# Initialize tracking variables
initial_money = money
rolls = 0
max_money = money
roll_at_max = 0

# Simulate the game
while money > 0:
    rolls += 1

    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    # Check outcome
    if total == 7:
        money += 4
    else:
        money -= 1

    # Track highest amount and when it occurred
    if money > max_money:
        max_money = money
        roll_at_max = rolls

# Output the results
print(f"\nYou are broke after {rolls} rolls.")
print(f"You should have quit after {roll_at_max} rolls when you had ${max_money}.")