# Write your code here
import turtle

def drawFractalLine(t, distance, level):
    """Draws a Koch fractal line with the given turtle, distance, and level."""
    if level == 0:
        t.forward(distance)
    else:
        distance /= 3.0
        drawFractalLine(t, distance, level - 1)
        t.left(60)
        drawFractalLine(t, distance, level - 1)
        t.right(120)
        drawFractalLine(t, distance, level - 1)
        t.left(60)
        drawFractalLine(t, distance, level - 1)

def main():
    # Setup turtle window and turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    turtle.bgcolor("white")

    # Move turtle to starting position
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    # Set parameters
    distance = 300
    level = 3  # Change this number (e.g., 0–5) to see different levels

    # Draw the three sides of the snowflake
    for angle in [0, -120, 120]:
        t.setheading(angle)
        drawFractalLine(t, distance, level)

    # Hide turtle and finish
    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()