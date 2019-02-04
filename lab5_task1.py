import math 

class point:
    def __init__(self):
        self.a=0
        self.b=0

def dist_between_points(x,y):
        d1=x.a-y.a
        d2=x.b-y.b
        dist=math.sqrt(d1**2 + d2**2)
        return dist

a=point()
b=point()
print(a)
print(b)
print(a !=b)

p0=point()
p0.a=24
p0.b=28

p1=point()
p1.a=15
p1.b=20
print("distance")
print(dist_between_points(p1,p0))
