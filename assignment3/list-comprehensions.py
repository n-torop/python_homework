import csv

with open ("../csv/employees.csv", "r", newline="") as file:
    reader=csv.reader(file)

    employees_name=[row[1]+" "+row[2] for row in reader if not "employee_id" in row]
    print (employees_name)

    only_e_names=[el for el in employees_name if "e" in el]
    print (only_e_names)
   