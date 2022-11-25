import random

gameOn = True
count = 0

def playGame():
    global count
    num = int(input("\nEnter a Number: "))
    if (not (1 <= num <=6)):
        print("Invalid input")
        return
    random = genRand()
    if random == num:
        print("Correct")
        count +=5
    else:
        print("Wrong")
    
    print(f"Your score is: {count}")

def genRand():
    return random.randint(1,6)

while True:
    playGame()
    ch =  input("\nEnter 'yes' to play again or 'no' to quit: ").lower()
    if(ch=='yes'):
        continue
    else:
        break