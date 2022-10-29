#You need to write a python script that generates an acronym word from a given sentence.
#•	Take multiple strings as input in the form of list.
#•	Add the first letter of each string to output.
#•	Iterate over the complete string and add every next letter to space to output.
#•	Change the output to uppercase (required acronym).
#•	You have to generate acronyms for all given strings.

#input = {"multiple string", "multiple strings", "Multiple words"} wrong inpot
#input2 = {"one","word","String"} currect input
i = input("Enter the sentence")
b =i
b=b.strip()
count = 0
li = list(b.split(" "))

j  = 0
while(j<len(b)):
	if(b[j] == " "):
		count+=1
	j+=1	

realCount = (count+1)
main = " "
for v in range(realCount):
	main = main+li[v][0]

print("acronym is:",main.upper())