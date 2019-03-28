from turtle import *
class Pole():
    def __init__(self,name,stack,top_position,x_pos,y_pos,thickness,length,color ):
        self.name = name
        self.stack = stack
        self.x = x_pos
        self.y = y_pos
        self.thick = thickness
        self.length = length
        self.color = color
        self.stack = []
        self.top_position = 0
    def showpole(self):
        sethead(0)
        pendown()
        for i in range (2):
            fd(20)
            lt(90)
            fd(150)
            lt(90)
    def pushdisk(self,disk):
        self.top_position -= 1
        disk
    def popdisk(self):
        pass

