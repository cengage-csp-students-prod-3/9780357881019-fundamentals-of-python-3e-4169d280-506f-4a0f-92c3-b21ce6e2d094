"""
File: studentapp.py
The application for editing and analyzing student scores.
"""

from student import Student
from studentview import StudentView

def main():
    """Creates the model and view and starts the app."""
    model = Student("Ken", 10)
    StudentView(model).mainloop()

if __name__ == "__main__":
    main()