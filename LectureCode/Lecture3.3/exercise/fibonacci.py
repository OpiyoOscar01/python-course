# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Counter to keep track of how many numbers we've printed
count = 0

# We want the first 10 numbers
while count < 10:
    print(a)
    # Update Fibonacci numbers
    a, b = b, a + b
    count += 1
