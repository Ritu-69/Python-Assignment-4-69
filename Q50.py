# Importing functions from both modules in the package
from mypackage.math_ops import add, multiply
from mypackage.string_ops import to_uppercase, reverse_string

# Using functions from math_ops
sum_result = add(10, 5)
prod_result = multiply(4, 3)

# Using functions from string_ops
upper_text = to_uppercase("hello world")
rev_text = reverse_string("python")

# Displaying outputs
print("Addition:", sum_result)
print("Multiplication:", prod_result)
print("Uppercase:", upper_text)
print("Reversed:", rev_text)
