import csv
import pandas as pd

file_name = "students.csv"

# Returning Student Details in DataFrame Format...
def view_students():
    with open(file_name, "r") as file:
        reading = list(csv.DictReader(file))

        # for i in reading:
        #     print(i)
        # print(reading)            will give in list format

        if not reading:                     # If CSV file is empty it handles it
            print("No CSV File Found")
            return

        student_data = pd.DataFrame(reading)
        # converting marks to Float
        student_data["Marks"] = student_data["Marks"].astype(float)
        return student_data
        