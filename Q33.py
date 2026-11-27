def largest_in_list(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage:
print(largest_in_list([14, 89, 23, 56, 3]))  # Output: 89
