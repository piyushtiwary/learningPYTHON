side1 = float(input("Enter the 1st side"))
side2 = float(input("Enter the 2nd side"))
side3 = float(input("Enter the 3rd side"))

s = ((side1+side2+side3)/2)

area = (s*(s - side1)*(s - side2)*(s - side3))**(1/2)

print(area)