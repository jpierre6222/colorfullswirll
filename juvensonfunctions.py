import turtle

turtle.colormode(255)

bob = turtle.Turtle()
      
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
bob = turtle.Pen() 
turtle.bgcolor('black')
bob.speed(1000)
for times in range(720): 
    bob.pencolor(colors [times%6] ) 
    bob.width(times/100 + 1) 
    bob.forward(times) 
    bob.left(59)
    bob.penup()
    bob.goto(95,100)
    bob.pendown()
    

    
bob = turtle.Turtle()
colors = ["red","purple","blue","green","orange","yellow",]
import random
bob.speed(5000)
bob.width(6)

for times in range(360):
	color = randomchoice(colors)
	bob.color(color)
	bob.forward(100)
	bob.right(30)
	bob.forward(20)
	bob.left(60)
	bob.forward(50)
	bob.right(30)
	
	bob.penup()
	bob.setposition(0, 0)
	bob.pendown()
	
	bob.right(1)
	
turtle.done()




for times in range(360):
    bob.color("purple")
    bob.left(75)
    bob.forward(250)
    bob.right(35)
    bob.forward(27)
    bob.left(40)
    bob.forward(80)
    bob.right(55)
    bob.penup()
    bob.setposition(8, 9)
    bob.pendown()
    bob.right(3)
turtle.done()

def spikeflower():
    turtle.Tracer(False)
for times in range(40):
    spikeflower(80 - times * 40)
    turtle.tracer(True)
        

def spike(distance):
    for times in range(20):
        bob.width(times * 12)
        bob.forward(distance)
        bob.left(10)
    
def tile(c):
    poylgon(4,200,c)
    for times in range(4):
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        polygon(3,50,"black")
        bob.forward(50)
        bob.left(90)
        

def triangle(distance):
    for times in range(3):
        bob.forward(distance)
        bob.left(120)

def poylgon(distance):
    sides = 5
    angle = 360 / sides
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(angle)
        bob.end_fill()
       
def jump(x,y):
    bob.penup()
    bob.goto(100,100)
    bob.pendown()

def circle(distance,c):
    bob.color( c )
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
    bob.end_fill()

    
def fadingtriangle(distance):
    for times in range(50):
        c = (250 - times * 5250 - times * 5, 0 )
        polygon(1, 450 - times * 8, c)
        
        
    




    





    
    
