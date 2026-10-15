"""
Task 3: PerformanceAnalyzer class
Accepts a list of KCAStudent objects and works out class-level results.
Also contains a helper to load the CSV (Task 1) into KCAStudent objects.
"""
import os
import pandas as pd
from task2_student import KCAStudent

# The CSV is found relative to this file, so it works wherever you run it from
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "task1_students.csv")

def load_students(path=DATA_FILE):
    """Read the CSV and return a list of KCAStudent objects."""
    df = pd.read_csv(path)
    return [
        KCAStudent(r["StudentID"], r["FName"], r["LName"],
                   r["Math"], r["English"], r["Science"])
        for _, r in df.iterrows()
    ]

class PerformanceAnalyzer:
    def __init__(self, students):
        self.students = students          # list of KCAStudent objects

    def highest_average(self):
        return max(self.students, key=lambda s: s.calculate_average())

    def lowest_average(self):
        return min(self.students, key=lambda s: s.calculate_average())

    def class_average(self):
        total = sum(s.calculate_average() for s in self.students)
        return total / len(self.students)

if __name__ == "__main__":
    analyzer = PerformanceAnalyzer(load_students())
    best = analyzer.highest_average()
    worst = analyzer.lowest_average()
    print(f"Highest average: {best.fname} {best.lname} "
          f"({best.calculate_average():.2f})")
    print(f"Lowest average : {worst.fname} {worst.lname} "
          f"({worst.calculate_average():.2f})")
    print(f"Class average  : {analyzer.class_average():.2f}")