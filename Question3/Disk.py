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
        
        color(2,0,0)
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
    
    def newpos(self,x,y):
        self.x = x
        self.y = y
        penup()
        goto(self.x,self.y)
    
    def cleardisk():
        pendown()
        color(255,255,255)
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


