from turtle import *
from random import*
import math

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

  k = Turtle()
tracer(1)

def drawCircle(centerX, centerY, radius, color):
  #by gargaar
    k.penup()
    k.goto(centerX,centerY)
    k.setheading(0)
    k.forward(radius)
    k.right(90)
    k.fillcolor(color)
    k.begin_fill()
    k.pendown()
    for i in range(360):
        k.forward(2*math.pi*radius/360)
        k.right(1)
    k.end_fill()

    
   
  def drawRoad():
    #By Bukhari Farah
          k.pencolor("Black")
          k.fillcolor("Black")
          k.pendown()
          k.begin_fill()
          k.pencolor
          k.forward(300)
          k.left(90)
          k.forward(100)
          k.left(90)
          k.forward(400)
          k.left(90)
          k.forward(100)
          k.left(90)
          k.forward(400)
          k.left(90)
          k.forward(30)
          k.left(90)
          k.forward(400)
          k.right(90)
          k.forward(50)
          k.right(90)
          k.forward(400)
          k.end_fill()

    
def drawMan():
    # by Bukhari
    tracer(0)
    k.setheading(0)
    k.left(90)
    k.forward(100)
    k.right(90)
    k.forward(50)
    k.right(180)
    k.forward(100)
    k.right(180)
    k.forward(50)
    k.right(90)
    k.forward(100)
    k.left(45)
    k.forward(75)
    k.right(180)
    k.forward(75)
    k.left(45)
    k.forward(75)
    k.right(180)
    k.forward(75)
    k.left(90)
    k.forward(125)
    k.right(90)
    k.circle(30)
    update()
 
ben = Turtle()

def HotAirBalloon():

  #made by Katherina
  
    colormode(255)

    def colour():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r,g,b)

    tracer(10)

    def balloon():

        ben.fillcolor(colour())
        ben.begin_fill()
        for i in range(405):
            ben.forward(2)
            ben.left(1)
        ben.end_fill()

    def basket():
        ben.right(135)
        ben.forward(100)
        ben.fillcolor(colour())
        ben.begin_fill()
        ben.left(90)
        ben.forward(20)
        ben.right(135)
        ben.forward(90)
        ben.right(45)
        ben.forward(60)
        ben.right(45)
        ben.forward(90)
        ben.right(135)
        ben.forward(180)
        ben.end_fill()
        ben.backward(173)
        ben.left(90)
        ben.forward(100)

    def OrbOfHeat():
        ben.fillcolor("orange")
        ben.begin_fill()
        for i in range(360):
            ben.left(1)
            ben.forward(0.15)
        ben.end_fill()

    def fireholder():
        ben.right(135)
        for i in range(30):
            ben.forward(2)
            ben.left(1)
        ben.right(75)
        ben.forward(25)
        ben.left(90)
        ben.forward(35)
        OrbOfHeat()
        ben.forward(35)
        ben.left(90)
        ben.forward(35)


    balloon()
    basket()
    fireholder()

    update()

 #all colour functions made by Katherina ahaha
    
  def randRed():
    #Made by Katherina
    r1 = randint(127, 255)
    g1 = randint(0, 63)
    b1 = randint(0, 63)

    return (r1, g1, b1)

def randOrange():
    #Made by Katherina
    r2 = randint(192, 255)
    g2 = randint(63, 127)
    b2 = randint(0, 63)

    return (r2, g2, b2)

def randYellow():
    #Made by Katherina
    r3 = randint(192, 255)
    g3 = r3
    b3 = randint(0, 63)

    return (r3, g3, b3)

def randGreen():
    #Made by Katherina
    r4 = randint(63, 127)
    g4 = randint(192, 255)
    b4 = randint(63, 127)

    return (r4, g4, b4)

def randBlue():
    #Made by Katherina
    r5 = randint(0, 63)
    g5 = randint(0, 63)
    b5 = randint(192, 255)

    return (r5, g5, b5)

def randViolet():
    #Made by Katherina
    r6 = randint(63, 127)
    g6 = randint(0, 63)
    b6 = randint(192, 255)

    return (r6, g6, b6)

tracer(20)

def squares(colour):
    #Made by Katherina
    def square():
        ben.setheading(90)
        ben.fillcolor(colour)
        ben.begin_fill()
        for i in range(4):
            ben.forward(32)
            ben.right(90)
        ben.right(90)
        ben.forward(32)
        ben.end_fill()
    square()

update()

def colourValues:
    #Made by Katherina
    red = randRed()
    orange = randOrange()
    yellow = randYellow()
    green = randGreen()
    blue = randBlue()
    violet = randViolet()

    squares(red)
    squares(orange)
    squares(yellow)
    squares(green)
    squares(blue)
    squares(violet)

    print("Random red :")
    print(red)
    print("Random orange :")
    print(orange)
    print("Random yellow :")
    print(yellow)
    print("Random green :")
    print(green)
    print("Random blue :")
    print(blue)
    print("Random violet :")
    print(violet)
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
drawCircle(100,100,55,"red")

drawBalloon()
drawStarFish()
drawSeaweed()    
drawMan()
HotAirBalloon()
drawRoad()

update()
