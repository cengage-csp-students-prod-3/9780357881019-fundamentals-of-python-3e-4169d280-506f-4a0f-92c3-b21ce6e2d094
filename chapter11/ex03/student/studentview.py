"""
File: studentview.py
The view for editing and analyzing student scores.
"""

from breezypythongui import EasyFrame

class StudentView(EasyFrame):

    def __init__(self, model):
        """Creates and lays out window components
        to view and manipulate the model's data."""
        EasyFrame.__init__(self)
        self.setSize(500, 200)
        self.model = model
        self.addLabel("Mean", row = 0, column = 0)            
        self.addLabel("Median", row = 1, column = 0)            
        self.addLabel("Mode", row = 2, column = 0)            
        self.addLabel("Standard deviation", row = 3, column = 0)
        self.meanFld = self.addFloatField(0.0, row = 0, column = 1, precision = 2)            
        self.medianFld = self.addFloatField(0.0, row = 1, column = 1, precision = 2)            
        self.modeFld = self.addFloatField(0.0, row = 2, column = 1, precision = 1)            
        self.stdFld = self.addFloatField(0.0, row = 3, column = 1, precision = 4)                        

        self.addLabel("Data", row = 0, column = 2, sticky = "NEW")
        self.scoreArea = self.addTextArea(text = "", row = 1, column = 2,
                                          width = 12, rowspan = 3)

        # Button panel
        bp = self.addPanel(row = 4, column = 0, columnspan = 3, background = "black")
        bp.addButton("Edit score", row = 0, column = 0, command = self.editScore)
        bp.addButton("Add score", row = 0, column = 1, command = self.addScore)
        bp.addButton("Delete score", row = 0, column = 2, command = self.deleteScore)
        bp.addButton("Randomize scores", row = 0, column = 3, command = self.randomizeScores)

        self.refreshData()

        bp = self.addPanel(row = 4, column = 0,
                    columnspan = 3,
                    background = "black")
        bp.addButton(text = "Edit score", row = 0, column = 0, command = self.editScore)
        bp.addButton(text = "Add score", row = 0, column = 1, command = self.addScore)
        bp.addButton(text = "Delete score", row = 0, column = 2, command = self.deleteScore)
        bp.addButton(text = "Randomize scores", row = 0, column = 3, command = self.randomizeScores)

        bp.addButton(text = "Plot scores",
             row = 0, column = 4,
             command = self.plotScores)
        
        def plotScores(self):
    """Displays a line plot of the student’s test scores."""
    import matplotlib.pyplot as plt

    scores = self.model.getScores()

    # X-axis positions (1, 2, 3, ...)
    positions = list(range(1, len(scores) + 1))

    # Create plot
    plt.figure()
    plt.plot(positions, scores, marker="o")
    plt.title(f"{self.model.getName()}'s Scores")
    plt.xlabel("Position")
    plt.ylabel("Score")
    plt.grid(True)
    plt.show()


    def refreshData(self):
        """Updates the view with the contents of the model."""
        self.setTitle(self.model.getName() + "'s Scores")
        self.meanFld.setNumber(self.model.getMean())
        self.medianFld.setNumber(self.model.getMedian())
        self.modeFld.setNumber(self.model.getMode())
        self.stdFld.setNumber(self.model.getStd())
        self.scoreArea.setText(str(self.model))

    # --------------------------------
    # Event-handling methods
    # --------------------------------

    def editScore(self):
        """Obtains a new score and its position from the user
        and updates the model and the view."""
        # Ask for the score position
        pos = self.prompterBox(title="Edit Score",
                               promptString="Position of the score to edit:")
        if pos is None:
            return

        newScore = self.prompterBox(title="Edit Score",
                                    promptString="New score value:")
        if newScore is None:
            return

        try:
            self.model.setScore(int(pos), float(newScore))
            self.refreshData()
        except Exception as e:
            self.messageBox(title="Error", message=str(e))

    def addScore(self):
        """Obtains a new score from the user,
        adds it to the model, and updates the view."""
        newScore = self.prompterBox(title="Add Score",
                                    promptString="Enter new score:")
        if newScore is None:
            return

        try:
            self.model.addScore(float(newScore))
            self.refreshData()
        except Exception as e:
            self.messageBox(title="Error", message=str(e))

    def deleteScore(self):
        """Obtains the position of a score from the user,
        deletes the score at that position from the model,
        and updates the view."""
        position = self.prompterBox(title = "Delete score",
                                    promptString = "Position of the score:")
        if position is None:
            return

        try:
            self.model.deleteScore(int(position))
            self.refreshData()
        except Exception as e:
            self.messageBox(title="Error", message=str(e))

    def randomizeScores(self):
        """Obtains the number of scores, lowest score,
        and highest score from the user, randomizes the model's scores,
        and updates the view."""
        num = self.prompterBox(title="Randomize Scores",
                               promptString="How many scores?")
        if num is None:
            return

        low = self.prompterBox(title="Randomize Scores",
                               promptString="Lowest possible score?")
        if low is None:
            return

        high = self.prompterBox(title="Randomize Scores",
                                promptString="Highest possible score?")
        if high is None:
            return

        try:
            self.model.randomize(int(num), float(low), float(high))
            self.refreshData()
        except Exception as e:
            self.messageBox(title="Error", message=str(e))
