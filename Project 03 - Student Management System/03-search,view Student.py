import csv
import pandas as pd
from view_students import view_students

file_name = "students.csv"

# Storing the function to another variable
view_students_Data = view_students
        
print(view_students_Data())

# ------------------------------------------------------------------------
# Search Student --> Not Returning anythin; Print all the Details directly
def searchStudent(id):
    final_list = []
    with open(file_name, "r") as file:
        reading = list(csv.DictReader(file))
        final_list = list(filter(lambda x:int(x["ID"])== id, reading))  

    # If final_list has No Matching Data
    if not final_list:              # as [] is False in Python
        print("Student not Found")
        return
    
    print("--------------------------")
    print(f"Details of Student {id}")
    # Problem : Here final_list is [{},{}] -- If multiple Match came
    for item in final_list:
        print(f"Students Name : {item["Name"]}")
        print(f"Students Marks : {item["Marks"]}")
        print("--------------------------")
searchStudent(1)

