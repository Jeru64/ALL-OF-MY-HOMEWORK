import math

angle = float(input("Enter angle in degrees: "))

# convert degrees → radians
radians = math.radians(angle)

# calculate values
sin_val = math.sin(radians)
cos_val = math.cos(radians)
tan_val = math.tan(radians)

print("sin(", angle, ") =", sin_val)
print("cos(", angle, ") =", cos_val)
print("tan(", angle, ") =", tan_val)
