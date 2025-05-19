
import turtle

a = turtle.Turtle()

def black(size):
  a.begin_fill()
  a.color('black','black')
  a.forward(size)
  a.left(90)
  a.forward(size)
  a.left(90)
  a.forward(size)
  a.left(90)
  a.forward(size)
  a.end_fill()
  a.left(90)
  a.forward(size)

def white(size):
   a.begin_fill()
   a.color('black','white')
   a.forward(size)
   a.left(90)
   a.forward(size)
   a.left(90)
   a.forward(size)
   a.left(90)
   a.forward(size)
   a.end_fill()
   a.left(90)
   a.forward(size)

def nextLine(size):
  a.left(90)
  a.forward(size)
  a.left(90)
  a.penup()
  a.forward(size*8)
  a.pendown()
  a.right(180)


def row1(size):
  for i in range(4):
    black(size)
    white(size)

def row2(size):
  for i in range(4):
    white(size)
    black(size)

size = 90

a.right(90)
a.forward(size*4)
a.right(90)
a.forward(size*4)
a.right(180)

for j in range(4):
  row1(size)
  nextLine(size) 
  row2(size)
  nextLine(size) 



turtle.done()