import csv

# with open('customers.csv', mode='r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open('access_logs.csv', mode='r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# with open('students.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(f"Name: {row['Name']}, Score: {row['Score']}")
        # print(row)

        
# with open('students.csv', mode='r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if int(row['Score']) > 80:
#             print(f"{row['Name']} passed with {row['Score']}")

# data = [['Name', 'Score'], ['Ada', 88], ['Bola', 76]]

# with open('output.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# # import csv

# students = [
#     {'Name': 'Ada', 'Subject': 'Math', 'Score': 88},
#     {'Name': 'Bola', 'Subject': 'Science', 'Score': 76},
#     {'Name': 'Chidi', 'Subject': 'English', 'Score': 92}
# ]

# with open('students_output.csv', mode='w', newline='') as file:
#     fieldnames = ['Name', 'Subject', 'Score']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
    
#     writer.writeheader()  # Write the header row
#     writer.writerows(students)

# profiles = [
#     {'First Name': 'Chibuzo', 'Last Name': 'Emmanuel', 'D.O.B': '14 Oct. 1994', 'Course': "Data Engr."},
#     {'First Name': 'Happines', 'Last Name': 'Okafor', 'D.O.B': '12 March 1999', 'Course': "AI & Prompt Engr."},
#     {'First Name': 'Esther', 'Last Name': 'Dike', 'D.O.B': '14 April 2002', 'Course': "Data Engr."}
# ] 

# with open("profile.csv", mode='w', newline="") as file:
#     fieldnames = ['First Name', 'Last Name', 'D.O.B', 'Course']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerows(profiles) 

# with open('profile.csv', mode= 'r') as file:
#     reader = csv.DictReader(file)
#     next(reader)
#     for row in reader:
#         #print(f"First Name:{row['First Name']} Last Name:{row['Last Name']} D.O.B:{row['D.O.B']} Course:{row['Course']}")
#         print(row)

# new_profiles = [
#     ['David', 'Elizerbirth', '14 Oct. 1997', "Edu. Chemistry"],
#     ['Mba', 'Jennifer', '13 March 1997', "HIR"],
#     ['Christopher',  'Chima',  '14 April 1995',  "Accounting"]
# ] 

# with open('profile.csv', '+a', newline='\n', encoding='utf-8')  as file:
#     writer= csv.writer(file)
#     writer.writerows(new_profiles)
#     print("appending successful")

data = [
    {1, "Admin", "Mechanical"}, 
    {2, "CEO", 'Electrical'},
    ]

# with open('csv_file.csv', '+a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#     print('Appended')


# new_data = {1, 'Snr. Pro.', 'IT'}
    
# with open('csv_file.csv', 'a',newline='') as file:
#     writer = csv.writer(file, delimiter= "|")
#     writer.writerows(new_data)
#     print('Another one')

import pandas as pd
import os


# try:
#     df = pd.read_csv("profile.csv")
#     print('Successfully read data.csv')
# except FileNotFoundError:
#     print('Error: The file does not exist!')

# df_new = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y']})
# df_new.to_csv('new_data.csv', index=False, mode='w')

# df_append = pd.DataFrame({'A': [3], 'B': ['z']})
# df_append.to_csv('new_data.csv', index=False, mode='a', header= False)

# df_sc = pd.read_csv('semi_colon.csv', sep=';')

# print('---DataFrame with Semicolon Delimiter ---')
# print(df_sc)

# df_append = pd.DataFrame({'ID': [101], 'Name': 'Femi', "Score": [90.2]})
# df_append.to_csv('semi_colon.csv', index=False, mode='a', header= False, sep=';')

# df_read = pd.read_csv("semi_colon.csv",)
# print(df_read)
# print("Successfully Read!!!")

# df_missing = pd.DataFrame({
#     'Temp_C': [25, 28, None, 22, 26],
#     'City': ['London', 'Paris', 'Berlin', 'Rome', None]
# })

# df_dropped = df_missing.dropna()
# print(df_dropped)

# df_reading = pd.read_csv('semi_colon.csv')
# read = df_reading.dropna()
# print(read)



# x = range(0,100,2)
# print(tuple(x))
# z= []
# x= range(0,100,2)
# for i in x:
#     z.append(i)
#     print(z)

# x = 2
# while x < 100:
#     print(x)
#     x += 2
# from openpyxl.workbook import workbook

# df_convert = pd.DataFrame({
#     'Item': ['Apple', 'Banana'],
#     'Price': [1.00, 0.50]
# })

# data = df_convert.to_json(orient='records', indent=4)
# print(data)

# data = df_convert.to_excel('data.xlsx', sheet_name='Products', index=False)

import csv
# import json

# csv_file = 'students.csv'
# json_file = 'students.json'

# data = []
# with open(csv_file, mode='r') as cf:
#     reader = csv.DictReader(cf)
#     for row in reader:
#         data.append(row)

# with open(json_file, mode='w') as jf:
#     json.dump(data, jf, indent= 4)

# with open('students.csv', mode='r') as cf:
#     rd = csv.DictReader(cf)
#     students = list(rd)
#     print(students)

# with open("students.csv", mode="r") as file:
#     reader = csv.DictReader(file,)

#     for row in reader:
#         if int(row["Score"]) > 80:
#             print(row)


with open('students.csv', mode="r") as file:
    rre = csv.DictReader(file)
    for line in rre:
        print(len(line))