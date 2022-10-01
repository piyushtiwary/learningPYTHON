# defining funtion 
def myFunSum(v, k):
  sum = v+k
  return sum
 
def myFunSub(v, k):
	sub = v-k
	return sub

def myFunMulty(v,k):
	multi = v*k
	return multi

def myFunDiv(v,k):
	div = v/k
	return div

# Calling funtions
userInput = int(input(" \n Enter 1 for Sum \n Enter 2 for Subtraction \n Enter 3 for Division \n Enter 4 for Multiplication"))

if(userInput == 1):
	var1 = int(input("Enter 1st number"))
	var2 = int(input("Enter 2nd number"))
	Output = myFunSum(var1,var2)
	print(Output)

elif(userInput == 2):
	var1 = int(input("Enter 1st value"))
	var2 = int(input("Enter 2nd value"))
	Output = myFunSub(var1,var2)
	print(Output)

elif(userInput == 3):
	var1 = int(input("Enter 1st value"))
	var2 = int(input("Enter 2nd value"))
	Output = myFunDiv(var1,var2)
	print(Output)

elif(userInput == 4):
	var1 = int(input("Enter 1st value"))
	var2 = int(input("Enter 2nd value"))
	Output = myFunMulty(var1,var2)
	print(Output)

else:
	print("Wrong Input")