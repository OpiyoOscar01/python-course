numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
  if number % 2 == 0:
    continue  # Skips the rest of the loop for even numbers.
  print(f"Current number is: {number}")