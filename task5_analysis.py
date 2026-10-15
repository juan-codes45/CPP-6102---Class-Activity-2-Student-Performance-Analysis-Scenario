"""
Task 5: Data Science Analysis using Pandas and Matplotlib
1. Load dataset  2. Average per student  3. Top, lowest, class average
4. Bar chart of student averages (saved as task5_averages.png)
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# 1. load
df = pd.read_csv(os.path.join(HERE, "task1_students.csv"))

# 2. average score for every student
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)
print(df[["StudentID", "FName", "LName", "Average"]].round(2))

# 3. insights
top = df.loc[df["Average"].idxmax()]
low = df.loc[df["Average"].idxmin()]
class_avg = df["Average"].mean()

print()
print("Top performer   :", top["FName"], top["LName"], round(top["Average"], 2))
print("Lowest performer:", low["FName"], low["LName"], round(low["Average"], 2))
print("Class average   :", round(class_avg, 2))

# 4. visualise
plt.figure(figsize=(7, 4))
plt.bar(df["FName"], df["Average"], color="steelblue")
plt.axhline(class_avg, color="red", linestyle="--", label="Class average")
plt.title("Student Average Scores")
plt.xlabel("Student")
plt.ylabel("Average score")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(HERE, "task5_averages.png"))
plt.show()