def check1(N):
	if 360 % N ==0:
		Case1 = True
	else:
		Case1 = False

	return Case1

def check2(N):
	if N < 360:
		Case2 = True
	else:
		Case2 = False

	return Case2

def check3(N):
	if N <= 26:
		Case3 = True
	else:
		Case3 = False

	return Case3

i = int(input("Enter The Number of Cuts"))

print("Case 1 ", check1(i))
print("Case 2 ", check2(i))
print("Case 3 ", check3(i))