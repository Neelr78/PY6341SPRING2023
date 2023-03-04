# Full Name: Neel Raval
# Student ID: 1099835
# Assignment Due Date: 2/20/23, 11:59 PM (CST)
# MSITM 6341:
# Assignment #4
# Assignment Title: working_with_for_loop
# working_with_for_loop.py



first_names = ['alice', 'bob', 'charlie', 'dave', 'eve', 'frank', 'grace', 'hank', 'isabelle', 'jack']
last_names = ['smith', 'johnson', 'lee', 'lee', 'brown', 'lee', 'wang', 'kim', 'davis', 'smith']
scores = [78, 92, 85, 76, 89, 91, 83, 77, 88, 90]


# 1. Print the entire first name, last name using for loop.
for names in first_names,last_names:
    print(names)

# 2. Print the first name and last name on the same output line (first letter must be capital)
print("\nStudent Full Name:")
print("------------------")

for i in range(len(first_names)):
    print(first_names[i].title() + " " + last_names[i].title())

# 3. Print the first name and last name in capital letter
print("\nStudent Full Name:")
print("------------------")

for i in range(len(first_names)):
    print(first_names[i].upper() + " " + last_names[i].upper())

# 4. Remove 3rd item (element) in the all three list.

first_names.pop(2)
last_names.pop(2)
scores.pop(2)
# 5. Add a new student information (first name, last name and score) on 8th index for each of the three list.

first_names.insert(8, 'jane')
last_names.insert(8, 'doe')
scores.insert(8, 95)

# Print the first name, last name and score (first letter must be capital)

print("\nStudent Full Name and Score:")
print("------------------")

for i in range(len(first_names)):
    print(first_names[i].title() + " " + last_names[i].title() +" -- "+ str('{:.2f}'.format((scores[i]))))

# 6. Sort the first name list and print each first name in one line
print("\nList of All Students First Name (Sorted):")
print("---------------------------------------------------")
first_names.sort()
for name in first_names:
    print(name.title())

print()
# 7.Create a new tuple with first five elements of student first name list and print that
first_five = first_names[:5]
print(first_five)
