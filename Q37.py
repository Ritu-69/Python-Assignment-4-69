greeting = "Welcome to Python!"  # Global variable


def show_global():
    print("Inside function:", greeting)


show_global()
print("Outside function:", greeting)
