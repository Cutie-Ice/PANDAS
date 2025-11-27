import json


# with open('student.json', 'r') as file:
#     data = json.load(file)
#     print(data['name'])
#     print(data['age'])
#     print(data['courses'])


import json

student_data = {
    "name": "Chidi",
    "age": 23,
    "courses": ["History", "Literature"]
}

# with open('student.json', 'w') as file:
#     json.dump(student_data, file, indent=4)

import json

# student = {"name": "Ada", "age": 25}
# json_string = json.dumps(student, indent=2)

# print(json_string)

# import json

# data = '''
# {
#   "user": {
#     "id": 1,
#     "name": "John Doe",
#     "details": {
#       "age": 28,
#       "location": "USA",
#       "hobbies": ["reading", "cycling"]
#     }
#   }
# }
# '''

# parsed = json.loads(data)
# print(parsed["user"]["name"])  # Output: John Doe
# print(parsed["user"]["details"]["age"])  # Output: 28
# print(parsed["user"]["details"]["hobbies"][1][::-1])
# print(parsed["user"]["details"]["location"])

import json

data = '''
{
    "students": [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78}
    ]
}
'''

# parsed = json.loads(data)
# for student in parsed["students"]:
#     print(f"{student['name']}: {student['score']}")

# data1 = {
#     "employee": {
#         "name": "John",
#         "department": {"name": "Engineering", "floor": 3},
#         "address": {"city": "Lagos", "country": "Nigeria"}
#     }
# }

# flat_data = {
#     "name": data1["employee"]["name"],
#     "department_name": data1["employee"]["department"]["name"],
#     "department_floor": data1["employee"]["department"]["floor"],
#     "city": data1["employee"]["address"]["city"],
#     "country": data1["employee"]["address"]["country"]
# }

# print(flat_data)

# data2 = {
#     "Id": 1,
#     "name": "John",
#     "address": {
#         "street": "123 Main St",
#         "city": "New York",
#         "state": "NY"
#     },
#     "contacts": [
#         {"type": "email", "value": "john@example.com"},
#         {"type": "phone", "value": "123-456-7890"}
#     ]
# }
# flat_data2 = {
#     "id": data2["Id"],
#     "name": data2["name"],
#     "add_street": data2["address"]["street"],
#     "add_city": data2["address"]["city"],
#     "add_state": data2["address"]["state"],
#     "con_type": data2["contacts"][0]["type"],
#     "con_value": data2["contacts"][0]["value"],
#     "con_type2": data2["contacts"][-1]["type"], 
#     "con_value2": data2["contacts"][-1]["value"]
#  }
# print(flat_data2)


# import json
# import csv

# with open('students.json', 'r') as json_file:
#     data = json.load(json_file)

# with open('students.csv', 'w', newline='') as csv_file:
#     if data:
#         fieldnames = data[0].keys()
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)


import json

# with open("students.json", 'r') as file:
#     loading = json.load(file)
#     print(loading)
#     with open('new_stud.json', 'w', newline='') as file:
#         json.dump(loading, file, indent=2, sort_keys=True)

#     print("Data written to file!")

    
# import json
# from urllib.request import urlopen

# with urlopen("") as response:
#     source = response.read()

# data = json.loads(source)
# print(data)

class_b = ["Dalington", "Emeka", 'Cynthia']
joining = ' '.join(class_b)
print(joining)