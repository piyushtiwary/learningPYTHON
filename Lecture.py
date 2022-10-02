import math
x = int(input("Enter the 1st side of of the triangle"))
y = int(input("Enter the 2nd side of of the triangle"))
z = int(input("Enter the 3rd side of of the triangle"))

s = (x+y+x)/2
ini = int(s(s-x)*(s-y)*(s-z))
area = int(math.sqrt(ini))
print(area)