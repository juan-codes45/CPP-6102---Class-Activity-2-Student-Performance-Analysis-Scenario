"""
Task 6: Report generation
ReportAnalyzer extends PerformanceAnalyzer (Task 3) and adds generate_report().
The report is printed and saved to task6_report.txt.
"""
import os
from task3_analyzer import PerformanceAnalyzer, load_students

HERE = os.path.dirname(os.path.abspath(__file__))

class ReportAnalyzer(PerformanceAnalyzer):
    def generate_report(self, filename=None):
        if filename is None:
            filename = os.path.join(HERE, "task6_report.txt")

        lines = ["STUDENT PERFORMANCE REPORT", "=" * 40]
        for s in self.students:
            lines.append(f"{s.student_id}  {s.fname} {s.lname:<10} "
                         f"Avg: {s.calculate_average():.2f}  Grade: {s.get_grade()}")

        best, worst = self.highest_average(), self.lowest_average()
        lines.append("-" * 40)
        lines.append(f"Top student    : {best.fname} {best.lname} "
                     f"({best.calculate_average():.2f})")
        lines.append(f"Lowest student : {worst.fname} {worst.lname} "
                     f"({worst.calculate_average():.2f})")
        lines.append(f"Class average  : {self.class_average():.2f}")

        report = "\n".join(lines)
        print(report)
        with open(filename, "w") as f:
            f.write(report)
        return report


if __name__ == "__main__":
    analyzer = ReportAnalyzer(load_students())
    analyzer.generate_report()