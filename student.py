class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)


