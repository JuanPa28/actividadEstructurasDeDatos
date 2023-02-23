from student import Student

__name__ == '__main__'

info_students = [
    {"name": "Juan", "age": 20, "grades": [5, 4.9, 4.2, 4.1, 4.7]},
    {"name": "Pablo", "age": 19, "grades": [3.2, 3, 2.9, 5, 4.8]},
    {"name": "Maria", "age": 18, "grades": [5, 5, 5, 5, 5]},
    {"name": "Karla", "age": 22, "grades": [0.9, 3.5, 2.4, 4, 1.1]},
    {"name": "Dorlan", "age": 25, "grades": [1, 1, 1, 0.9, 5]},
]

new_student = [Student(i["name"], i["age"], i["grades"]) for i in info_students]

print("Student")
for student in new_student:
    print(student)