from turtle import *

bgcolor('black')

penup()
goto(-300,0)
left(180)
pendown()
 

def heartbeat():
    bgcolor('black')
    pencolor('white')
    x= 0
    y= 0  
    while x<10:
        x=x+1
        left(180)
        forward(10)
        left(80)
        forward(50)
        


heartbeat()



penup()
pencolor('white')
fillcolor('red')

goto(-100, 0)
pendown()
width(2)
goto(-50, 50)
goto(0,0)
penup()
goto(-70,30)
pendown()
goto(-30,30)
left(-120)

begin_fill()
circle(-50)
end_fill()