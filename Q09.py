import math

angle_deg = float(input("Enter angle in degrees: "))

# Convert degrees to radians before using trig functions
angle_rad = math.radians(angle_deg)

print("Sine:", round(math.sin(angle_rad), 4))
print("Cosine:", round(math.cos(angle_rad), 4))
print("Tangent:", round(math.tan(angle_rad), 4))
