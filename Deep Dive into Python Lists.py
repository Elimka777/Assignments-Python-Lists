students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
#Filter out students who have grades below 80. Print the name, grade and activiy.
for name, grade, activity in zip(students, grades, activities):
    if grade <= 80:
        print(name, grade, activity)
#For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]
students_approved = [student for student, grade in zip(students, grades) if grade >=80]
print(f"Approved students: {students_approved}")