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
