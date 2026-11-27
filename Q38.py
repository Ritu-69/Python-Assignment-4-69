x = 10  # Global variable


def test_scope():
    x = 5  # Local variable with the same name
    print("Inside function (local x):", x)


test_scope()
print("Outside function (global x):", x)
