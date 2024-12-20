import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.bgcolor('lightpink')

t_ground = turtle.Turtle()
t_ground.penup()
t_ground.pencolor('white')
t_ground.fillcolor('white')
t_ground.speed(0)
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

# creat the turtle
snowman = turtle.Turtle()
snowman.speed(3)

t_ground.penup()
t.ground.goto(0,100)
t_ground.fillcolor('white')
t_ground.begin_fill()
t_ground.circle(25)
t_ground.end_fill()
t_ground.pendown()

snowman.penup()

#This is the last line of code
turtle.done()