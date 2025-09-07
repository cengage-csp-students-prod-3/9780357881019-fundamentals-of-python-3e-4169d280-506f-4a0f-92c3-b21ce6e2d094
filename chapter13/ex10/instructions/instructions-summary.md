<!-- manual -->

## Instructions

The function that draws c-curves, and which was discussed in Chapter 8, has two recursive calls. Here is the code:

```python
def cCurve(t, x1, y1, x2, y2, level):
    def drawLine(x1, y1, x2, y2):
    """Draws a line segment between the endpoints."""
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    if level == 0:
        drawLine(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)
```

You can assume that the function `drawLine` runs in constant time. State the computational complexity of the `cCurve` function, in terms of the level, using big-O notation. Also, draw a call tree for a call of this function with a level of 3. (LO: 13.2, 13. 6))

## Your Tasks
