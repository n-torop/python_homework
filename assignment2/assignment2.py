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
import custom_module
def set_that_secret(upd_secret):
    custom_module.set_secret(upd_secret)
    return custom_module.secret
# print(set_that_secret("ice cream"))

#Task 12
def read_minutes():
    min1_dict={}
    min1_list=[]

    min2_dict={}
    min2_list=[]

    data_file1="../csv/minutes1.csv"
    data_file2="../csv/minutes2.csv"

    with open(data_file1, "r") as file1:
        reader=csv.reader(file1)
        for index, row in enumerate(reader):
            if index==0:
                min1_dict["fields"]=row
            if index!=0:
                min1_list.append(tuple(row))
        min1_dict["rows"]=min1_list

    with open(data_file2, "r") as file2:
        reader=csv.reader(file2)
        for index, row in enumerate(reader):
            if index==0:
                min2_dict["fields"]=row
            if index!=0:
                min2_list.append(tuple(row))
        min2_dict["rows"]=min2_list
    
    return min1_dict, min2_dict
   
minutes1, minutes2=read_minutes()

# Task 13
def create_minutes_set():
    joint_set=set()
    for key, val in minutes1.items():
        if type(val)==list:
            min1_set=set(val)

    for key, val in minutes2.items():
        if type(val)==list:
            min2_set=set(val)
    joint_set=min1_set.union(min2_set)
    return joint_set


minutes_set=create_minutes_set()
# print(minutes_set)

#Task 14
from datetime import datetime

def create_minutes_list():
    new_list=[]
    upd_minutes_list=list(minutes_set)
    def convert(string):
        return datetime.strptime(string, "%B %d, %Y")

    for name, date in upd_minutes_list:
        date_converted=convert(date)
        tuple_pair=(name, date_converted)
        new_list.append(tuple_pair)
    return new_list
               
minutes_list=create_minutes_list()
# print(minutes_list)

#Task 15
def write_sorted_list():
    sorted_list=[]
    def convert(og_date):
        return datetime.strftime(og_date, "%B %d, %Y")
    sorted_data=sorted(minutes_list, key=lambda tup: tup[1])
    # print (sorted_data)
    for name, date in sorted_data:
        date_converted=convert(date)
        tuple_pair=(name, date_converted)
        sorted_list.append(tuple_pair)
  
    with open ("./minutes.csv", "w", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(sorted_list)
    
    return sorted_list


print(write_sorted_list())
