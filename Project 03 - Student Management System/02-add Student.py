import csv
import pandas as pd
from view_students import view_students

file_name = "students.csv"
student_data = view_students()
print(student_data)


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

# ! Will add ; add_student to prevent duplicate IDs

# 05-Nov -- Created search_students function separately and imported here
# it's returning a dataframe(pandas) of all students...now i need to get it and check and prevent duplicates in addStudent