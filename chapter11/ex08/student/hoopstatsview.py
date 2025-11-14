from breezypythongui import EasyFrame
import matplotlib.pyplot as plt

class HoopStatsView(EasyFrame):

    def __init__(self, frame):
        """Creates the window with radio buttons for all stats columns."""
        EasyFrame.__init__(self, title="Basketball Statistics Viewer")
        self.frame = frame
        self.setSize(600, 400)

        # Label
        self.addLabel("Select a Statistic to Plot:", row=0, column=0, columnspan=2)

        # The radio button group
        self.statGroup = self.addRadiobuttonGroup(row=1, column=0, rowspan=20)

        # Add radio buttons for each numeric column except name/team
        numeric_columns = [
            col for col in frame.columns
            if frame[col].dtype != "object"
        ]

        # Add each remaining column as a radio button
        for col in numeric_columns:
            self.statGroup.addRadiobutton(text=col)

        # Default selection
        self.statGroup.setSelectedButton(self.statGroup.getButton(0))

        # Plot button
        self.addButton("Plot", row=1, column=1, command=self.plotStat)


    def plotStat(self):
        """Plots the currently selected statistic."""
        col = self.statGroup.getSelectedButton()["text"]

        plt.figure()
        plt.plot(self.frame[col])
        plt.title(f"{col} Across All Games")
        plt.xlabel("Game Index")
        plt.ylabel(col)
        plt.show()

        import matplotlib.pyplot as plt

def plotStat(self):
    """Analyzes the selected column and displays a line plot."""
    
    # Get the selected statistic
    col = self.statGroup.getSelectedButton()["text"]
    
    # --- Existing analysis code (mean, median, etc.) ---
    data = self.frame[col]
    mean = data.mean()
    median = data.median()
    std = data.std()

    # Display results in the GUI (your labels may differ)
    self.meanField.setText(f"{mean:.2f}")
    self.medianField.setText(f"{median:.2f}")
    self.stdField.setText(f"{std:.2f}")

    # --- New requirement: pop up a line plot ---
    plt.figure()
    plt.plot(data)
    plt.title(f"{col} Over Time")
    plt.xlabel("Game Index")
    plt.ylabel(col)   # Required by the exercise
    plt.tight_layout()
    plt.show()

