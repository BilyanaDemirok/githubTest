import random
import turtle
deny = turtle.Pen()

deny.width(4)
deny.speed(-5)

colorlist = ['black', 'grey']

def square(size):
    for i in range(20):
        deny.forward(size)
        deny.left(90)
        
for i in range(100):
    x = random.randrange(-200,200)
    y = random.randrange(-200,200)
    deny.up()
    deny.goto(x, y)
    deny.down()
    col = random.choice(colorlist)
    deny.color(col)
    square(random.randrange(10, 200))

