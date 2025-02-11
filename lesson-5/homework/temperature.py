def convert_cel_to_far(c):
    return c*1.8+32

def convert_far_to_cel(f):
    return (f-32)/1.8

f = float(input("Enter a temperature in degrees F:"))
print(f'{f} degrees F = {convert_far_to_cel(f):.2f} degrees C')

c = float(input("Enter a temperature in degrees C:"))
print(f'{c} degrees C = {convert_cel_to_far(c):.2f} degrees F')