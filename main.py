from turtle import Turtle,Screen
import random


scr = Screen()
scr.setup(width=500,height=400)
color_choosen = scr.textinput(title = "welcome to Turtle race",prompt =" choose the color of the turtle that you think will win.")
print(color_choosen)
colors = ["violet","blue","green","yellow","orange","red"]
timmy = [0,0,0,0,0,0]
y_cor = -100
for i in range(6):
    timmy[i] = Turtle()
    timmy[i].shape("turtle")
    timmy[i].penup()
    rand_color = random.choice(colors)
    timmy[i].color(rand_color)
    colors.remove(rand_color)
    timmy[i].goto(x=-230,y=y_cor)
    y_cor+=40
race_notfinished = True
while race_notfinished:
    rand_turtle = random.randint(0,5)
    timmy[rand_turtle].forward(10)
    if timmy[rand_turtle].xcor()==230:
        winner = timmy[rand_turtle]
        race_notfinished = False
if winner.color() == color_choosen:
    print(f"You won the bet, {color_choosen} turtle is the winner.")
else:
    print(f"You lost the bet, {winner.color()[0]} turtle is the winner.")


scr.exitonclick()
