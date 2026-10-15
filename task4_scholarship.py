"""
Task 4: Inheritance
ScholarshipStudent inherits from KCAStudent (the base class named in Task 2).
Extra attribute: scholarship_amount. Extra method: is_eligible().
Eligibility rule: average score >= 85.
"""
from task2_student import KCAStudent

class ScholarshipStudent(KCAStudent):
    def __init__(self, student_id, fname, lname, math, english, science,
                 scholarship_amount):
        super().__init__(student_id, fname, lname, math, english, science)
        self.scholarship_amount = scholarship_amount

    def is_eligible(self):
        return self.calculate_average() >= 85

if __name__ == "__main__":
    # scholarship amounts are sample values for testing only
    students = [
        ScholarshipStudent("25/222", "Sandra", "Mutegi", 75, 80, 70, 50000),
        ScholarshipStudent("25/224", "Carlos", "Ndunda", 90, 85, 88, 50000),
        ScholarshipStudent("25/226", "Paul", "Omboga", 60, 65, 58, 50000),
        ScholarshipStudent("25/228", "Ruth", "Mwimali", 95, 92, 90, 50000),
    ]
    for s in students:
        print(f"{s.fname:<8} average {s.calculate_average():.2f}  "
              f"grade {s.get_grade()}  eligible: {s.is_eligible()}")