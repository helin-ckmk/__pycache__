from turtle import *
import time
w=Screen()
w.setup(300,700)
w.title("Trafik Işık Uygulaması")

penup()
goto(0,180)
pendown()
pensize(4)

for i in range(2):
    forward(80)
    right(90)
    forward(220)
    right(90)

def kirmizi():
    penup()
    goto(40,140)
    fillcolor("red")
    shape("circle")
    shapesize(3)

def sari():
    penup()
    goto(40,70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)

def yesil():
    penup()
    goto(40,0)
    fillcolor("green")
    shape("circle")
    shapesize(3)

calis=True

while calis:
    yesil()
    time.sleep(2)
    sari()
    time.sleep(2)
    kirmizi()
    time.sleep(2)

    calis=False

w.mainloop()

    
