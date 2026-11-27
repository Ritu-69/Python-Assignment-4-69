import math

# Input values
x = 3
y = 4
angle_deg = 30

# Convert degrees to radians for trigonometric functions
angle_rad = math.radians(angle_deg)

# Calculate expression: sqrt(x^2 + y^2) + sin(30°)
result = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) + math.sin(angle_rad)

print("Result of the expression:", round(result, 2))
