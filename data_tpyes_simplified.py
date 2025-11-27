data_entries = ["filename", "label", "brand", "topic", "theme", "method", "gift", "fist", "small", "best"]
print("First 3 words: ", data_entries[:3])
print("Last 3 words: ", data_entries[-3:])
print("The middle Words: ", data_entries[3:7])

letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
print(letters[::-1])
User_choice = int(input("Enter a Number: "))
convert_calc = User_choice * 2
data_entries.append(convert_calc)
print("Updated list: ", data_entries)
print("Calc result: ", convert_calc)