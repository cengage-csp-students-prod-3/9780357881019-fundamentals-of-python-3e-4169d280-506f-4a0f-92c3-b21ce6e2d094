"""
File: chessboard.py
Displays an 8 by 8 grid of black and white squares of a chessboard.
"""

from breezypythongui import EasyFrame

class Chessboard(EasyFrame):

    def __init__(self):
        """Sets up the window and the panels."""
        EasyFrame.__init__(self, title = "Chess",
                           width = 200, height = 200)
        color = "white"
        for row in range(8):
            for column in range(8):
                if color == "black":
                    color = "white"
                else:
                    color = "black"
                self.addPanel(row = row, column = column,
                              background = color)

def main():
    """Instantiate and pop up the window."""
    Chessboard().mainloop()

if __name__ == "__main__":
    main()
