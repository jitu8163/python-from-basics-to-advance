import math

x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))

p1=[x1,y1]
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))

p2=[x2,y2]

d=(((x2-x1)**2)+(y2-y1)**2)**0.5
print("Distance between the given points is: ", d)
