class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def avarage_grade(self):
        promedio= sum(self.grades) / len(self.grades)
        return promedio

    info_students = [
        {"nombre": "Juan", "edad": 20, "grades": [5, 4.9, 4.2, 4.1, 4.7]},
        {"nombre": "Pablo", "edad": 19, "grades": [3.2, 3, 2.9, 5, 4.8]},
        {"nombre": "Maria", "edad": 18, "grades": [5, 5, 5, 5, 5]},
        {"nombre": "Karla", "edad": 22, "grades": [0.9, 3.5, 2.4, 4, 1.1]},
        {"nombre": "Dorlan", "edad": 25, "grades": [1, 1, 1, 0.9, 5]},
    ]
