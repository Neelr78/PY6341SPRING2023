# Full Name: Neel Raval
# Student ID: 1099835
# Assignment Due Date: 3/26/23, 11:59 PM (CDT)
# MSITM 6341:
# Assignment : 7
# Assignment Title: working_with_input_and_while
# working_with_input_and_while.py

prompt = "Please enter 'quit' in the name field to stop the user input."
print(prompt)

Employee_details = {}
while True:
    employee_name = input("Enter Employee Name : ")
    if employee_name.strip().lower() == 'quit':
        break
    monthly_income = float(input("Enter Your Monthly income : "))
    Employee_details[employee_name] = monthly_income
    if len(Employee_details) < 10:
        continue
    else:
        break

print("Employee Name\t\t\t""Employee Salary")
print("-" * 45)

total_salary = 0
for name,income in Employee_details.items():
    print(f"{name}\t\t\t${income:,.2f}")
    total_salary = sum(Employee_details.values())

print("-" * 45)
print(f"Total Salary Expense\t\t${total_salary:,.2f}") 
print("=" * 45)

if len(Employee_details) == 0:
    print("No data found.")
elif len(Employee_details) < 10:
    print("Enter at least 10 employee's data.")
else:
    highest_earning_employee = max(Employee_details, key=Employee_details.get)
    print(f"Highest Earning Employee is {highest_earning_employee}, salary: ${Employee_details[highest_earning_employee]:,.2f}")
    lowest_earning_employee = min(Employee_details, key=Employee_details.get)
    print(f"Lowest Earning Employee is: {lowest_earning_employee}, salary: ${Employee_details[lowest_earning_employee]:,.2f}")