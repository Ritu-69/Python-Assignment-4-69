def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage:
print(find_largest([10, 45, 2, 99, 23]))  # Output: 99
