"""
Task 2: KCAStudent class
Stores one student's details and marks, and calculates average and grade.
Encapsulation: attributes are private and exposed through read-only properties.
"""
class KCAStudent:
    def __init__(self, student_id, fname, lname, math, english, science):
        self.__student_id = student_id
        self.__fname = fname
        self.__lname = lname
        self.__math = math
        self.__english = english
        self.__science = science
    
    # read-only access to the private attributes
    @property
    def student_id(self):
        return self.__student_id

    @property
    def fname(self):
        return self.__fname

    @property
    def lname(self):
        return self.__lname

    @property
    def math(self):
        return self.__math

    @property
    def english(self):
        return self.__english

    @property
    def science(self):
        return self.__science

    def calculate_average(self):
        return (self.__math + self.__english + self.__science) / 3

    def get_grade(self):
        # Assumed grading scale (the brief did not give one)
        avg = self.calculate_average()
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        return "E"

if __name__ == "__main__":
    # quick test using Sandra's marks
    s = KCAStudent("25/222", "Sandra", "Mutegi", 75, 80, 70)
    print(s.fname, s.lname)
    print("Average:", round(s.calculate_average(), 2))
    print("Grade  :", s.get_grade())