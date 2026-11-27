def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Can accept any number of arguments
print(add_all(10, 20, 30))      # Output: 60
print(add_all(5, 15, 25, 35))   # Output: 80
