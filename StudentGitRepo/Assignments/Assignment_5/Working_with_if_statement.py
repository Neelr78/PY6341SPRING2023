# Full Name: Neel Raval
# Student ID: 1099835
# Assignment Due Date: 3/5/23, 11:59 PM (CST)
# MSITM 6341:
# Assignment #5
# Assignment Title: working_with_if_statement
# working_with_if_statement.py


full_name = "Neel Raval"
name2 = ""
name3 = ""

print()

# Step 3
print("My Full name is "+ full_name.title())

#Step 4
print("----------------------------")
print()

# Step 5
for letter in full_name:
    
    if letter.isupper():
        letter = letter.lower()
    else:
        letter = letter.upper()
    print(f"ASCII value of {letter} is {ord(letter)}")
    
    name2 +=  letter + "-"
    
    name3 += str(ord(letter)) + "-" 

print()
#Step 6
print("-" +name2)
print("-" +name3)
#Step 7

print("----------------------------")