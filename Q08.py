import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

gcd_val = math.gcd(a, b)
lcm_val = math.lcm(a, b)

print("GCD:", gcd_val)
print("LCM:", lcm_val)
