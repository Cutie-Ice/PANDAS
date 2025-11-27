student_scores_list = [
    {"name": "Happiness", "score": 75},
    {"name": "Kingsley", "score": 50},
    {"name":  "mathew", "score": 65},
    {"name": "Evelin", "score": 105},
    {"name": "Mendy", "score": 15},
    {"name": "Sarah", "score": -10}
]
count_pass = 0
count_fail = 0
count_invalid = 0

for student in student_scores_list:
    if student["score"] < 0 or student["score"] > 100:
        count_invalid += 1
        print(f"This is an invalid score!")
        continue
    if student["score"] >= 60:
        count_pass += 1
        print(f"{student["name"]}: {student["score"]} PASS")
    else:
        count_fail += 1
        print(f"{student['name']}: {student['score']} FAIL")
print(f"Total students passed: {count_pass}")
print(f"Total students Failed: {count_fail}")
print(f"Total invalid scores: {count_invalid}")