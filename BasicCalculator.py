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
print(" \n Enter 1 for Sum \n Enter 2 for Subtraction \n Enter 3 for Division \n Enter 4 for Multiplication")
userInput = int(input())

if(userInput == 1):
	print("Enter 2 numbers")
	var1 = int(input())
	var2 = int(input())
	Output = myFunSum(var1,var2)
	print(Output)

elif(userInput == 2):
	print("Enter 2 numbers")
	var1 = int(input())
	var2 = int(input())
	Output = myFunSub(var1,var2)
	print(Output)

elif(userInput == 3):
	print("Enter 2 numbers in A/B order")
	var1 = int(input())
	var2 = int(input())
	Output = myFunDiv(var1,var2)
	print(Output)

elif(userInput == 4):
	print("Enter 2 numbers")
	var1 = int(input())
	var2 = int(input())
	Output = myFunMulty(var1,var2)
	print(Output)

else:
	print("Wrong Input")