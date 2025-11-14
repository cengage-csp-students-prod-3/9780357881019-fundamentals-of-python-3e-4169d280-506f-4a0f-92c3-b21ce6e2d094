"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd


def cleanStats(df):
    """
    Cleans FG, 3PT, and FT columns in the dataset by:
        - Removing the original column containing 'makes-attempts' strings.
        - Splitting each into two separate integer columns: Makes and Attempts.
        - Inserting new columns into the correct positions.
    Returns the cleaned DataFrame.
    """

    # Columns to be converted: "x-y" → two columns
    stats_to_clean = ["FG", "3PT", "FT"]

    # Mapping to new column names
    new_names = {
        "FG": ("FGM", "FGA"),
        "3PT": ("3PTM", "3PTA"),
        "FT": ("FTM", "FTA")
    }

    for col in stats_to_clean:
        if col in df.columns:

            # Get position of original column
            idx = df.columns.get_loc(col)

            # Split "x-y" format
            split_col = df[col].astype(str).str.split("-", expand=True)

            # Convert to integers (fill missing with 0)
            makes = pd.to_numeric(split_col[0], errors="coerce").fillna(0).astype(int)
            attempts = pd.to_numeric(split_col[1], errors="coerce").fillna(0).astype(int)

            # New column names
            m_col, a_col = new_names[col]

            # Insert the new columns
            df.insert(idx, m_col, makes)
            df.insert(idx + 1, a_col, attempts)

            # Drop the old "makes-attempts" column
            df.drop(columns=[col], inplace=True)

    return df


def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")

    # Clean the FG, 3PT, and FT columns BEFORE passing to the view
    frame = cleanStats(frame)

    HoopStatsView(frame).mainloop()


if __name__ == "__main__":
    main()
