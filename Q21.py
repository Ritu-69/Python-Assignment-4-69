def sum_of_digits(n):
    n = abs(n)  # Handle negative numbers
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Example usage:
print(sum_of_digits(1234))  # Output: 10
