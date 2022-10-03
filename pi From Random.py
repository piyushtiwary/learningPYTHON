import random

points = int(input("Enter the number of points "))

dots_in_circle = 0
dots_in_square = 0

# counting number of random dots 
for _ in range(points):
	x = random.uniform(0,1)
	y = random.uniform(0,1)
	distance = x**2 + y**2
	if(distance<=1):
		dots_in_circle +=1 
	dots_in_square +=1

# calculating pi
pi = 4* dots_in_circle/dots_in_square

print(pi)
	