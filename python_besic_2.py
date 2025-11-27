# students = {
#     "Emmanuel": "Salvador",
#     "Chibuzo": "Favour Lodge",
#     "Somtochukwu": "J&J",
#     "Jennifer": "Marvelous"
# }

# for student in students: 
    # print(student, students[student], sep=":") 
 
while True:

    try:
        x = int(input("what's x: "))
        break
    except ValueError:
        print("x is not an int")
        

print(f"x is{x}  ")
 