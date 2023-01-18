from turtle import Turtle, Screen
import random
tim =Turtle()
my_screen = Screen()
my_colors =  ["red", "purple", "brown", "pink", "green"]
tim.speed("fastest")
# for i in range(4):
#     tim.fd(100)
#     tim.left(90)


# #dashes line
# for i in range (20):
#     tim.forward(5)
#     tim.up()
#     tim.forward(5)
#     tim.down()
 
# #concentric shapes

# for i in range(3,11):
#     angle = 360/i
#     for j in range(i):
#         tim.fd(80)
#         tim.left(angle)


# #maze
# for i in range(40):
#     tim.color(random.choice(my_colors))
#     tim.forward(5+i*10)
#     tim.left(90)


#Random Walk

ts_choices = [0,90,180,270]
tim.pensize(10)

for i in range(200):
    tim.color(random.choice(my_colors))
    tim.setheading(random.choice(ts_choices))
    tim.forward(20)

my_screen.exitonclick()