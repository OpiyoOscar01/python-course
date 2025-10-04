def divide_numbers(a, b):
    if b == 0:
      print("Error: Division by zero is not allowed.")
      return None
    return a / b
print(divide_numbers(10, 2))  # Outputs: 5.0
print(divide_numbers(10, 0))  # Outputs: Error message and None
print(divide_numbers(25, 5))  # Outputs: 5.0