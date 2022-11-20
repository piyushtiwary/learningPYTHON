email = input("Enter your E-mail")

count = 0

for i in range(len(email)):
	if email[i] != "@":
		count+=1
	else:
		break

userName = email[0:count]
domain = email[count+1:len(email)+1]

print("Your Usename Is" , userName)
print("Your domain is" ,domain.upper())