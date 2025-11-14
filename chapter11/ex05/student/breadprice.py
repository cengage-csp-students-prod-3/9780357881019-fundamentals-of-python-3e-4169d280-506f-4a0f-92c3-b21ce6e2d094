# Write your code here
import pandas as pd
import matplotlib.pyplot as plt

# Load the data file manually downloaded from BLS
# Replace 'bread.csv' with the filename you downloaded
filename = "bread.csv"

# Read the CSV (skip header rows if needed depending on BLS format)
df = pd.read_csv(filename)

# Clean column names
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Drop columns not needed
keep_cols = ["Year"] + months
df = df[keep_cols]

# Convert all month columns to numeric
for m in months:
    df[m] = pd.to_numeric(df[m], errors="coerce")

# Fill missing values with the row mean
df[months] = df[months].apply(lambda r: r.fillna(r.mean()), axis=1)

# Compute yearly average price
df["Average"] = df[months].mean(axis=1)

print(df)

# Plot
plt.plot(df["Year"], df["Average"])
plt.xlabel("Year")
plt.ylabel("Average Price of Bread ($)")
plt.title("Average Price of Bread by Year")
plt.grid(True)
plt.show()
