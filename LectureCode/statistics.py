# statistics_from_file.py

def read_numbers(filename):
    """
    Reads numbers from a file and returns them as a list of floats.
    Handles errors if file doesn't exist or lines aren't numbers.
    """
    numbers = []
    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if line:  # ignore empty lines
                    try:
                        num = float(line)
                        numbers.append(num)
                    except ValueError:
                        print(f"Warning: Line {line_number} is not a valid number: '{line}'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
    return numbers

def calculate_statistics(numbers):
    """
    Returns a dictionary with sum, average, min, max of the list.
    """
    if not numbers:
        return {"sum": 0, "average": 0, "min": None, "max": None}
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return {"sum": total, "average": average, "min": minimum, "max": maximum}

def save_statistics(filename, stats):
    """
    Saves statistics to a file.
    """
    try:
        with open(filename, "w") as file:
            file.write("Statistics Results:\n")
            file.write(f"Sum: {stats['sum']}\n")
            file.write(f"Average: {stats['average']}\n")
            file.write(f"Minimum: {stats['min']}\n")
            file.write(f"Maximum: {stats['max']}\n")
        print(f"Statistics saved to '{filename}' successfully!")
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")

def main():
    input_file = input("Enter the name of the input file (with numbers): ")
    numbers = read_numbers(input_file)
    if not numbers:
        print("No valid numbers found. Exiting program.")
        return
    stats = calculate_statistics(numbers)
    
    print("\nCalculated Statistics:")
    print(f"Sum: {stats['sum']}")
    print(f"Average: {stats['average']}")
    print(f"Minimum: {stats['min']}")
    print(f"Maximum: {stats['max']}")

    output_file = input("Enter the name of the output file to save statistics: ")
    save_statistics(output_file, stats)

if __name__ == "__main__":
    main()
