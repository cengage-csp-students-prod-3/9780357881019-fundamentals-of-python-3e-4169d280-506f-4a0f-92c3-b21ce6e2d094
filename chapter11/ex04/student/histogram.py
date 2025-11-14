# Write your code here
"""
File: histogram.py
Displays the histogram shown in Figure 11-7.
(LO: 11.2)
"""

import matplotlib.pyplot as plt

def main():
    # Heights of the bars from the textbook figure
    data = [1, 3, 2, 5, 4]

    # X positions for each bar (1, 2, 3, 4, 5)
    positions = list(range(1, len(data) + 1))

    # Create the bar chart
    plt.figure()
    plt.bar(positions, data)

    # Title and axis labels
    plt.title("Histogram")
    plt.xlabel("Bar Number")
    plt.ylabel("Height")

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()
