user_input = input("Enter a string: ")
new_string = ""

for char in user_input:
    if char == " ":
        continue  # Skip spaces using the continue keyword
    new_string += char

print("Modified string:", new_string)
