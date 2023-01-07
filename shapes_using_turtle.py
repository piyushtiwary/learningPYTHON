import turtle

colors = ["blue", "red", "green", "yellow", "pink", "Orange", "Brown", "DarkKhaki", "Magenta", "Olive"]

timmi = turtle.Turtle()
timmi.pensize(3)

for i in range(1,7):
	timmi.pencolor(colors[i])
	for j in range(i+2):
		timmi.fd(80)
		timmi.rt(360/(i+2))
	
my_screen = turtle.Screen()

