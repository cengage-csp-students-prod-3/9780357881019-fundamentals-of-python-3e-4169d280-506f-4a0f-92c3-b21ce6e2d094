from turtle import Turtle, tracer, update
import random

def cCurve(t, x1, y1, x2, y2, level):
   
   def drawLine(x1, y1, x2, y2):
      """Draws a line segment between the endpoints using a random color."""
      # Generate random RGB color
      r = random.random()
      g = random.random()
      b = random.random()
      t.pencolor(r, g, b)
      t.up()
      t.goto(x1, y1)
      t.down()
      t.goto(x2, y2)
      
   if level == 0:
      drawLine(x1, y1, x2, y2)
   else:
      xm = (x1 + x2 + y1 - y2) / 2
      ym = (y1 + y2 - x1 + x2) / 2
      cCurve(t, x1, y1, xm, ym, level - 1)
      cCurve(t, xm, ym, x2, y2, level - 1)

def main():
   level = int(input("Enter the level (0 or greater): "))
   t = Turtle()
   t.hideturtle()
   t.speed(0)
   t.getscreen().colormode(1.0)  # Allow RGB colors in range 0–1
   if level > 8:
      tracer(False)
   cCurve(t, 50, -50, 50, 50, level)
   if level > 8:
      update()

if __name__ == "__main__":
   main()