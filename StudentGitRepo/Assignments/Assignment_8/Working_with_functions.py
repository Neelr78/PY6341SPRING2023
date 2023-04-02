# Full Name: Neel Raval
# Student ID: 1099835
# Assignment Due Date: 4/2/23, 11:59 PM (CDT)
# MSITM 6341:
# Assignment : 8
# Assignment Title: Working_with_functions
# Working_with_functions.py

def classify_temperature(temperature):
    if(temperature > 100):
        temp_classification = 'Very Hot weather'
        return temp_classification
    elif(temperature > 90 and temperature <= 100):
        temp_classification = 'Hot weather'
        return temp_classification
    elif(temperature > 80 and temperature <= 90):
        temp_classification = 'Warm'
        return temp_classification
    elif(temperature > 70 and temperature <= 80):
        temp_classification = 'Good weather'
        return temp_classification
    elif(temperature > 50 and temperature <= 70):
        temp_classification = 'Cold'
        return temp_classification
    elif(temperature > 32 and temperature <= 50):
        temp_classification = 'Very Cold'
        return temp_classification
    elif(temperature <= 32):
        temp_classification = 'Freeezing weather'
        return temp_classification


prompt = "Please enter 'done' in the city name field to stop the user input."
print(prompt)
temperature_data = {}

while True:    
    city = input("Enter city Name:")
    if(city.strip().lower() == 'done'):
        if(len(temperature_data) < 10):
            print("Enter at least 10 cities and their temperature")
        else:
            break
    else:
        temperature = int(input("Enter Temperature:"))
        temperature_data[city] = temperature

print("=" * 70)
print("City Name",end="\t" )
print("Temperature",end= "\t")
print("Temperature Classification")
print("=" * 70)

for name,temperature in temperature_data.items():
    print(name,end="\t\t")
    print(temperature,end="\t\t")
    temperature_classification = classify_temperature(temperature)
    print(temperature_classification)