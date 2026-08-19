name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height (in feet): ")) * 0.3048  # Convert height from feet to meters
rounded_height = round(height, 2)
print(f"Hello, my name is {name}! I am {age} years old and {rounded_height} meters tall.")
print(f"In 5 years, I will be {age + 5} years old.")