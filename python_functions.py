data_entries = ["sales.csv", "inventory.csv", "customers.csv"]
user_input = input("Enter a number: ")
calculation = int(user_input) + 2
data_entries.append(calculation)
print(f"Updated Data entries: {data_entries}")
print(f"Calculation result: {calculation}")
