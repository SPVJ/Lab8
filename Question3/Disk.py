from turtle import *


class Disk():
    def __init__(self,name,x,y,h,w):
        self.name = name
        self.x = x
        self.y =y
        self.h = h
        self.w = w
    
    def showdisk(self):
        pendown()
        
        color("black")
        seth(0)
        fd(self.w/2)
        left(90)
        fd(h)
        left(90)
        fd(w)
        left(90)
        fd(h)
        left(90)
        fd(self.w/2)
    
    def newpos(self,x,y):
        self.x = x
        self.y = y
        penup()
        goto(self.x,self.y)
    
    def cleardisk():
        pendown()
        color("white")
        seth(0)
        fd(w/2)
        left(90)
        fd(h)
        left(90)
        fd(w)
        left(90)
        fd(h)
        left(90)
        fd(w/2)


