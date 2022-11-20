import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

length_of_password = int(input("Enter the length of your password"))
numbers_of_numbers = int(input("How many numbers do you want in your password?"))
numbers_of_symbols = int(input("How many symbols do you want in your password?"))
numbers_of_letters = length_of_password - (numbers_of_numbers+numbers_of_symbols)

ranList = []

for i in range(numbers_of_letters):
	ranList += random.choice(letters) 

for j in range(numbers_of_numbers):
	ranList += random.choice(numbers)

for k in range(numbers_of_symbols):
	ranList += random.choice(symbols)

random.shuffle(ranList)

for char in ranList:
	print(char, end="")