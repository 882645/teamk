from turtle import *
from random import*

k = Turtle()

colormode(255)

def reminder():
  # by Mr. Riley
  # don't forget to put a comment with your name at the top of each function you make
  # this will help to keep track of who created each function
  return True

def drawSeaweed():
  #by gargaar
  for i in range(5):
    k.goto(100,-200)
    k.fillcolor("green")
    k.pendown()
    k.begin_fill()
    k.setheading(180)
    for i in range(5): 
      for i in range(90): 
        k.forward(.25)
        k.right(1)
      k.forward(20)
      for i in range(90):
        k.forward(.25)
        k.right(1)
      for i in range(90):
        k.forward(.25)
        k.left(1)
      k.forward(20)
      for i in range(90):
        k.forward(.25)
        k.left(1)
    k.hideturtle()
    k.end_fill()

def drawStarFish():
  #by gargaar
    k.goto(randint(-100,250), randint(-2,250))
    k.fillcolor("purple")
    k.begin_fill()
    k.pendown()
    for i in range(5): #code for the star
        k.left(144)
        k.forward(100)
    k.penup()
    k.end_fill()

def drawBalloon():
  k.fillcolor("purple")
  k.begin_fill()
  k.circle(100)
  k.setheading(-90)
  k.forward(200)
  k.end_fill()
  k.hideturtle()
  
def drawCar():
  # by kevin
  k.penup()
  k.goto(rand(-500,500)randint(-500,500))
  k.setheading(0)
  k.pendown()
  k.fillcolor("Green")
  k.begin_fill()
  k.forward(25)
  k.pendown()
  k.left(30)
  k.forward(50)
  k.right(30)
  k.forward(75)
  k.right(30)
  k.forward(50)
  k.left(30)
  k.forward(25)
  k.right(90)
  k.forward(50)
  k.right(90)
  k.forward(300)
  k.right(120)
  for i in range(100):
    k.right(0.5)
    k.forward(0.9)
  k.setheading(0)
  k.forward(25)
  k.end_fill()
  k.penup()
  k.forward(50)
  k.fillcolor("Blue")
  k.begin_fill()
  k.left(30)
  k.pendown()
  k.forward(35)
  k.setheading(0)
  k.forward(50)
  k.right(90)
  k.forward(17.5)
  k.right(90)
  k.forward(80)
  k.end_fill()
  k.penup()
  k.setheading(0)
  k.forward(80)
  k.right(90)
  k.forward(10)
  k.pendown()
  k.fillcolor("Black")
  k.begin_fill()
  k.forward(2.5)
  k.right(90)
  k.forward(15)
  k.right(90)
  k.forward(2.5)
  k.right(90)
  k.forward(15)
  k.end_fill()
  k.penup()
  k.forward(70)
  k.right(90)
  k.forward(25)
  k.setheading(0)
  k.forward(3)
  k.fillcolor("Red")
  k.begin_fill()
  k.pendown()
  for i in range(4):
    k.forward(7.5)   
    k.right(90)
  k.end_fill()
  k.penup()
  k.right(90)
  k.forward(10)
  k.right(90)
  k.forward(50)
  k.fillcolor("Black")
  k.pendown()
  k.begin_fill()
  k.circle(20)
  k.end_fill()
  k.penup()
  k.forward(175)
  k.pendown()
  k.begin_fill()
  k.circle(20)
  k.end_fill()
  k.penup()
  k.forward(72.5)
  k.pendown()
  k.fillcolor("Yellow")
  k.begin_fill()
  k.forward(2.5)
  k.right(90)
  k.forward(7.5)
  k.right(90)
  k.forward(9)
  k.end_fill()
  
def drawBoat():
  # by kevin
  k.pendown()
  k.fillcolor("Brown")
  k.begin_fill()
  k.forward(200)
  k.setheading(270)
  for i in range(180):
    k.forward(2)
    k.right(1)
  k.forward(2)
  k.setheading(0)
  k.forward(100)
  k.end_fill()
  k.left(90)
  k.forward(125)
  k.fillcolor("Red")
  k.right(120)
  k.begin_fill()
  k.forward(100)
  k.setheading(180)
  k.forward(87)
  k.end_fill()
  
def drawBird():
  # by kevin
  k.fillcolor(0,0,0)
  k.begin_fill()
  k.pendown()
  k.setheading(0)
  for i in range(30):
    k.forward(1)
    k.right(2)
  k.setheading(45)
  for i in range(30):
    k.forward(1)
    k.right(2)
  k.left(170)
  for i in range(30):
    k.forward(1)
    k.left(2)
  k.setheading(135)
  for i in range(30):
    k.forward(1)
    k.left(2)
  k.end_fill()


drawBalloon()
drawStarFish()
drawSeaweed()   
drawCar()
drawBoat()
drawBird()


update()
