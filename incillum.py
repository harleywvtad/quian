mixed_string = "a1b2c3d4e5"

letters = ''.join(filter(str.isalpha, mixed_string))
numbers = ''.join(filter(str.isdigit, mixed_string))

print("Letters:", letters)
print("Numbers:", numbers)
