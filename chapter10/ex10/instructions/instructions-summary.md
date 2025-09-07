<!-- manual -->

## Instructions

Geometric shapes can be modeled as classes. Develop classes for line segments,
circles, and rectangles in the **shapes.py** file. Each shape object should contain a `Turtle` object and a color that allow the shape to be drawn in a Turtle graphics window (see Chapter 8 for details).

Factor the code for these features (instance variables and methods)
into an abstract `Shape` class. The `Circle`, `Rectangle`, and `Line` classes are all subclasses of `Shape`. These subclasses include the other information about the specific types of shapes, such as a radius or a corner point and a `draw` method.

Write a script called **testshapes.py** that uses several instances of the different shape classes to draw a house and a stick figure. (LO: 10.1, 10.2, 10.4)

Set the starting position (x-axis, y-axis) of the main window to **(0,0)** by using the **turtle.setup()** function.

> Make sure to use the **turtle.done()** function as the last statement in your turtle graphics program.

An example of the program is shown below:

<p align="center">
    <img src="../assets/10.10.png" width="60%" alt="A Python Turtle Graphics window displaying a simple drawing on a white background. On the left, a black rectangle represents a house with a red angled roof and a small blue rectangle as a door. On the right, a black stick figure is drawn with a circle for a head, a vertical line for the body, horizontal line for arms, and two diagonal lines for legs.
">
</p>

## Your Tasks
