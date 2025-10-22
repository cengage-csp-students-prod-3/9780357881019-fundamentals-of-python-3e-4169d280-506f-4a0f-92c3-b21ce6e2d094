# Write your code here
import turtle
import random

def draw_rectangle(x, y, width, height, color):
    """Draw a filled rectangle with the given position, size, and color."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color("black", color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def mondrian(x, y, width, height, level=0):
    """
    Recursively subdivide the given rectangle into random colored sections.
    Alternates between vertical and horizontal splits.
    """
    # Base case: stop subdividing at an aesthetically right moment
    if width < 50 or height < 50 or random.random() < 0.2:
        draw_rectangle(x, y, width, height,
                       random.choice(["red", "blue", "yellow", "white", "black", "gray", "orange"]))
        return

    # Alternate splitting directions: even = vertical, odd = horizontal
    if level % 2 == 0:
        # Vertical split: 1/3 and 2/3 portions
        split = width / 3
        if random.random() < 0.5:
            split = width * 2 / 3
        mondrian(x, y, split, height, level + 1)
        mondrian(x + split, y, width - split, height, level + 1)
    else:
        # Horizontal split: 1/3 and 2/3 portions
        split = height / 3
        if random.random() < 0.5:
            split = height * 2 / 3
        mondrian(x, y, width, split, level + 1)
        mondrian(x, y + split, width, height - split, level + 1)

def main():
    """Set up the turtle and draw the Mondrian-style recursive pattern."""
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

    # Start with a large rectangle covering most of the screen
    screen_width = 600
    screen_height = 600
    start_x = -screen_width // 2
    start_y = -screen_height // 2

    mondrian(start_x, start_y, screen_width, screen_height)

    turtle.done()

if __name__ == "__main__":
    main()
