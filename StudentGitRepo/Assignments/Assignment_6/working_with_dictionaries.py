# Full Name: Neel Raval
# Student ID: 1099835
# Assignment Due Date: 3/19/23, 11:59 PM
# MSITM 6341:
# Assignment #6
# Assignment Title: working_with_dictionaries
# working_with_dictionaries.py

student_info = {}

student_names = ['Neel','Saun','Jenni','cardi','Mia','Wiz','Pac','justin','Ruby','Carter']
students_math_marks = [92.65,85.65,45.56,78.52,65.32,78.89,85.98,68.65,78.45,89.23]
students_english_marks = [85.63,78.56,25.32,75.64,78.45,85.25,69.96,89.36,97.68,78.65]
students_physics_marks = [36.56,78.21,36.36,75.63,98.63,89.32,78.31,63.21,74.65,69.98]
students_chemistry_marks = [34.45,36.68,65.45,89.65,45.74,56.74,78.89,98.62,41.42,65.23]

for i in range(len(student_names)):
    student_info[student_names[i]] = {}
    student_info[student_names[i]]["Math"] = students_math_marks[i]
    student_info[student_names[i]]["English"] = students_english_marks[i]
    student_info[student_names[i]]["Physics"] = students_physics_marks[i]
    student_info[student_names[i]]["Chemistry"] = students_chemistry_marks[i]


print("=" * 100)
print("Name\t\tMath\t\tEnglish\t\tPhysics\t\tChemistry\tTotal Marks")
print("-" * 100)

for key, value in student_info.items():
    print(key, end="\t\t")
    total_marks = 0
    for subkey,subvalue in value.items():
        total_marks += subvalue   
        print(subvalue, end= "\t\t")
    print("{:.2f}".format(total_marks))
