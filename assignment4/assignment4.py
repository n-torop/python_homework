import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
#Task 1
data={
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35], 
    "City": ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame=pd.DataFrame(data)
# print(task1_data_frame)

task1_with_salary=task1_data_frame.copy(deep=True)
task1_with_salary["Salary"]= [70000, 80000, 90000]
# print(task1_with_salary)

task1_older=task1_with_salary.copy(deep=True)
task1_older["Age"]+=1
# print(task1_older)

# task1_older.to_csv("employees.csv", index=False)

#Task 2
import json

task2_employees=pd.read_csv("employees.csv")
# print(task2_employees)

data_emp={"Name": ["Eve", "Frank"], 
          "Age": [28, 40], 
          "City": ["Miami", "Seattle"], 
          "Salary": [60000, 95000], 
          }

# with open("additional_employees.json", "w") as outfile:
#     json.dump(data_emp, outfile, indent=4)

json_employees=pd.read_json("additional_employees.json")
# print(json_employees.head())
more_employees=pd.concat([task2_employees, json_employees], ignore_index=True)
# print (more_employees)

#Task 3
first_three=more_employees.head(3)
# print (first_three)

last_two=more_employees.tail(2)
# print(last_two)

employee_shape=more_employees.shape
# print(employee_shape)

print (more_employees.info())

#TASK 4
dirty_data=pd.read_csv("dirty_data.csv")
# print(dirty_data)
clean_data=dirty_data.copy(deep=True)
clean_data=clean_data.drop_duplicates()

clean_data["Age"]=pd.to_numeric(clean_data["Age"], errors='coerce')
# print(clean_data)
clean_data["Salary"]=pd.to_numeric(clean_data["Salary"], errors='coerce')
placeholders=["unknown", "n/a"]
clean_data=clean_data.replace(placeholders, np.nan)
# print (clean_data)
mean_score=clean_data["Age"].mean()
clean_data["Age"]=clean_data["Age"].fillna(mean_score)
# clean_data["Salary"]=clean_data["Salary"].fillna(mean_score)
clean_data["Salary"]=clean_data["Salary"].fillna(clean_data["Salary"].median())
# print (clean_data)

clean_data["Hire Date"]=pd.to_datetime(clean_data["Hire Date"], errors="coerce", format="mixed")
# print(clean_data)

clean_data["Name"]=clean_data["Name"].str.strip()
clean_data["Name"]=clean_data["Name"].str.upper()

clean_data["Department"]=clean_data["Department"].str.strip()
clean_data["Department"]=clean_data["Department"].str.upper()
print(clean_data)

#      pytest -v -x assignment4-test.py