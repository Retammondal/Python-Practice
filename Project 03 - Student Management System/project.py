import csv

# ==================================================
# PROJECT: STUDENT MANAGEMENT SYSTEM
# TOPIC: PYTHON CSV FILE HANDLING
# ==================================================

# Created Basic Datasets 
data_rows = [
    [1, 'Retam', 90],
    [2, 'Rahul', 65],
    [3, 'Priya', 95]
]

with open("students.csv", "w", newline="") as file:
    writing = csv.writer(file)
    
    # writing.writeheader = ["ID", "Name", "Marks"]

    # Writing Header
    writing.writerow(["ID", "Name", "Marks"])
    # Writing Rest Rows
    writing.writerows(data_rows)

# -------------------------------------------------

file_name = "students.csv"

def add_student():
    name = input("Enter Student Name:").capitalize()
    idStud = int(input(f"Enter id of {name}:"))
    marks = float(input(f"Enter Marks obtained by {name}:"))

    with open(file_name, "a", newline="") as file:
        writing = csv.writer(file)

        writing.writerow([idStud, name, marks])
    print(f"Student {name},ID={idStud} with marks {marks}")
    print("Added Successfully")


add_student()
import pandas as pd
def view_students():
    with open(file_name, "r") as file:
        reading = list(csv.DictReader(file))

        # for i in reading:
        #     print(i)

        # print(reading)            will give in list format
        print(pd.DataFrame(reading))
        
view_students()

# Completed add_student and some part of view_student
# learnt that reader/Dictreader give in iterator just like map/filter -- convert to list to get in list format