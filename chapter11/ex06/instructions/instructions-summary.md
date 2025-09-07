<!-- manual -->

## Instructions

The columns labeled FG, 3PT, and FT of the data set in the _Analyzing Basketball Statistics_ case study do not show a single integer value but instead show values with the format <makes-attempts>, which is not suitable for the kind of data analysis performed on the other columns. For example, analysts might like to view the mean of free throws attempted as well as mean of the free throw percentage. You can correct this problem with a cleaning step that, for each such column:

- removes it from the data frame
- creates two new columns from this series, where the first column includes the numbers of makes and the second column includes the number of attempts
- inserts the new pairs of columns into the data frame at the appropriate positions, with the appropriate column headings (for example, FTM and FTA)

Define a function named `cleanStats` in the file **hoopstatsapp.py**. This function expects a data frame as an argument and returns the frame cleaned according to the steps listed previously. You should call this function after the frame is loaded from the CSV file and before it is passed to the `HoopStatsView` constructor. (LO: 11.2, 11.3)

An example of the program is shown below:
Before calling the `cleanStats` function on, the frame would look like:

<center>
<img src="../assets/chapter11ex06-1.png" alt="Before" width="400"/>
</center>

After calling the `cleanStats` function, the frame would look like:

<center>
<img src="../assets/chapter11ex06-2.png" alt="After" width="400"/>
</center>

## Your Tasks
