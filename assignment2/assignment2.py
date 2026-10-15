#Task 2
import csv

def read_employees():
    
    dict_employees={}
    list_employees=[]
    data_file="../csv/employees.csv"
    try:
        with open (data_file, "r") as file:
            reader=csv.reader(file)
            
            for index, row in enumerate (reader):
                if index==0:
                    dict_employees["fields"]=row
                if index!=0:
                    list_employees.append(row)
            dict_employees["rows"]=list_employees

                
        return dict_employees
        # print (list_employees)      
    except Exception as e:
        print (e)

employees=read_employees()


# Task 3
def column_index(string):
    info=employees["fields"]
    return info.index(string)

employee_id_column=column_index("employee_id")
# print(employee_id_column)

# Task 4
def first_name(row_num):
    selected_col=column_index("first_name")
    selected_name=employees["rows"][row_num][selected_col]
    return selected_name
        
# print(first_name(2))

# Task 5
def employee_find(employee_id): 
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"])) 
    return matches
# print (employee_find(3))

# Task 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


# Task 7
def sort_by_last_name():
    selected_col=column_index("last_name")
    employees["rows"].sort(key=lambda row: row[selected_col])
    return employees["rows"]
# print (sort_by_last_name())

# Task 8
def employee_dict(row):
    new_dict={}
    
    
    keys=employees["fields"]
    values=row
    for key, value in zip(keys, values):
        if key!="employee_id":
            new_dict[key]=value
    return new_dict
# print(employee_dict(employees["rows"][0]))

# Task 9
def all_employees_dict():
    full_employee_dict={}
    key_list=[]
    for key in employees["rows"]:
        key_list.append(key[0])
    value_list=[]
    for i in range (len(employees["rows"])):
        value_list.append(employee_dict(employees["rows"][i]))
    for key, value in zip(key_list, value_list):
        full_employee_dict[key]=value
    return full_employee_dict

    # print (value_list)

# print(all_employees_dict())

#Task 10
import os

def get_this_value():
    value=os.environ.get("THISVALUE")
    return value

# get_this_value()

#Task 11
