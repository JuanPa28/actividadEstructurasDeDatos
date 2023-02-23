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

    def __str__(self):
        return f"Nombre: {self.name}, Edad: {self.age}, Notas: {self.grades}"










