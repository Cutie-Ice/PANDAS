import string

def is_palindrome(s):
    # Normalize the string: remove punctuation, spaces, and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned = s.translate(translator).replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def check_palindromes(my_list):
    for item in my_list:
        if is_palindrome(item):
            print(f'"{item}" is a palindrome')
        else:
            print(f'"{item}" is not a palindrome')

# List to check
My_list = [
    'mummy',
    'hannah',
    'murder for a jar of red rum',
    'mom',
    'seagull',
    'tomato',
    'no lemon, no melon',
    'some men interpret nine memos',
    'madam'
]

# Run the check
check_palindromes(My_list)