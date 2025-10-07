# Creating  dictionary of student marks
student_marks = {
    "Sri": 85,
    "Ramya": 78,
    "Sanju": 92,
    "Meera": 74,
    "Hema": 88
}

# Ask the user for a student's name
name = input("Enter the student's name: ")

# Retrieve and display the marks if the student exists
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
print("\n Thankyou")
