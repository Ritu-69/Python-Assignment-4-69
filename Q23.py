def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage:
print(calculate_average([10, 20, 30, 40]))  # Output: 25.0
