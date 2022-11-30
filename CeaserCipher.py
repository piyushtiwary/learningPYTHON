def encrypt(sentance):
	new_sentence = ""
	for ch in sentance:
		new_sentence += chr(ord(ch)+9)
	return new_sentence

def decrypt(sentance):
	new_sentence = ""
	for ch in sentance:
		new_sentence += chr(ord(ch)-9)
	return new_sentence


while True:
	user_input = input("Enter Your Sentance\n")
	choice = input("Enter encrypt or decrypt\n").lower()

	if choice == "encrypt":
		print(encrypt(user_input)) 
	elif choice == "decrypt":
		print(decrypt(user_input))
	else:
		print("Wrong")

	YN = input("Enter Y if you wnat to continue or N id you want to stop\n").upper()
	if YN == "N":
		break

