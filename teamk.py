from turtle import *
from random import*

k = Turtle()

colormode(255)

def reminder():
  # by Mr. Riley
  # don't forget to put a comment with your name at the top of each function you make
  # this will help to keep track of who created each function
  return True
  
from turtle import *
from random import *

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

update()

drawSeaweed()    


update()
