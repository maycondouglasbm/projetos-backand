from turtle import *

color("red")
begin_fill()
pensize(5)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50,200)
forward(133)
end_fill()


penup()
goto(0, -40)  
pendown()


write("Milena", align="center", font=("Arial", 30, "normal"))

done()