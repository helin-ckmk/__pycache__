from turtle import *
pensize(3)
win=Screen()
win.setup(200,200)
penup()
def Nokta (x,y):
    goto(x,y)
    pendown()

win.onclick(Nokta)#Tıklama olduğunda Nokta fonksiyonunu çalıştırır
mainloop()
