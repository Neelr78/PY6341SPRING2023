# Full Name: Neel Raval
# Student ID: 1099835
# Assignment Due Date: 2/17/23, 11:59 PM (CST)
# MSITM 6341:
# Assignment #3
# Assignment Title: working_with_lists
# working_with_lists.py


City_names = ['Mumbai','Delhi','Ahmedabad','kolkata','Banglore','Chennai','Pune','Hydrabad','Surat','Kanpur']
Population = [12000000,11000000,3701800,4631400,5104050,4328060,2935745,2894500,2823249,3232249]

print(City_names)
print(Population)
print("Population of " + City_names[2] +" "+"is "+str(Population[2]))
print("Population of " + City_names[-1] +" "+"is "+str(Population[-1]))
City_names.insert(5,'Vadodara')
Population.insert(5,5600000)
print(City_names)
print(Population)
City_names.pop(3)
Population.pop(3)
print(City_names)
print(Population)
print(sorted(City_names))
print(sorted(Population))
Population[1] = Population[1] * 2 # step : 10




