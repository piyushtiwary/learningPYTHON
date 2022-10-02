# taking inputs
side1 = float(input("Enter the 1st side"))
side2 = float(input("Enter the 2nd side"))
side3 = float(input("Enter the 3rd side"))

# calculating semi_perimeter
s = ((side1+side2+side3)/2)

# calculating area
area = (s*(s - side1)*(s - side2)*(s - side3))**(1/2)

print(area)