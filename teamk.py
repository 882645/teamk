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
  #by gargaar
  k.fillcolor("purple")
  k.begin_fill()
  k.circle(100)
  k.setheading(-90)
  k.forward(200)
  k.end_fill()
  k.hideturtle()

drawBalloon()
drawStarFish()
drawSeaweed()    


update()
