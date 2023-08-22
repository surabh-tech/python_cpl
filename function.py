def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube


num = float(input("Enter a number: "))

square_result, cube_result = calculate_square_and_cube(num)

print(f"Square of {num}:", square_result)
print(f"Cube of {num}:", cube_result)
