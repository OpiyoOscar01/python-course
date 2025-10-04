area=18 # Global variable==Global scope.
y=14
def calculate_area(length, width):
    area = length * width # Local variable==Local scope
    print(y)
    return area


room_area=calculate_area(5, 4)
print(f"The calculated area of the room is {room_area} meters squared.")
print(area)  # This will raise an error since 'area' is not defined outside the function.
print(y)  # This will print the global variable y