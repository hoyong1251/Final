import math

class Point:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y

    def distance(self,other):
        x_dis=abs(self.__x - other.__x)
        y_dis=abs(self.__y - other.__y)
        dis=math.sqrt(x_dis*x_dis + y_dis*y_dis)
        return dis
    
    def __add__(self,other):
        self.__x+=other.__x
        self.__y+=other.__y
        return self

    def printPoint(self):
        print("[{0}, {1}]".format(self.__x, self.__y))

p1=Point(1,1)
p2=Point(2,2)


p1.printPoint()
p2.printPoint()

print(p1.distance(p2))

(p1+p2).printPoint()
