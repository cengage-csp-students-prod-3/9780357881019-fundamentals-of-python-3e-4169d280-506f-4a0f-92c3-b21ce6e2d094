# Write your code here
import math
import turtle

def drawCircle(t, x, y, radius):
    """Draws a circle with the given center (x, y) and radius using the Turtle object t."""
    
    # Move to the starting point of the circle (without drawing)
    t.penup()
    t.setposition(x + radius, y)  # Start at the rightmost point of the circle
    t.setheading(90)              # Point the turtle upward (tangent to the circle)
    t.pendown()
    
    # Calculate the distance to move each step
    step_length = 2.0 * math.pi * radius / 120.0  # circumference / 120
    
    # Draw the circle using 120 small steps (each turn is 3 degrees)
    for _ in range(120):
        t.left(3)
        t.forward(step_length)

# Example test code
if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    drawCircle(t, 0, 0, 100)  # Draw a circle centered at (0, 0) with radius 100

    screen.mainloop()  # Keep the window open