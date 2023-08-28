from shapely.geometry import Point
from shapely.geometry import LineString


def proyection( A ,  B ,  P):


    m= float((A.y - B.y)/(A.x - B.x))
    b = float(-B.x * m +  B.y)
    line = LineString([(-100 , float(m*(-100) + b)), (100, float(m*(100) + b))]) 

    dist = line.project(P)
    return list(line.interpolate(dist).coords)[0]


class Curva:
    A = Point(0,0)
    B = Point(0,0)
    C = Point(0,0)
    t = float(0)
    id = int(0) 

    def __init__(self , id , A , B , C , t ):
        self.id=id
        self.A=A
        self.B=B
        self.C=C
        self.t=t
    
    def normalize(self):

        D = Point(proyection( self.A, self.C,  self.B))
        AD = self.A.distance(D)
        BD = self.B.distance(D)
        CD = self.C.distance(D)
        AC = self.A.distance(self.C)
        x = float(0)

        factor = float(1/AC)
        if AD > CD :
            x = AD
        else:
            x =  AC - CD 

        self.A = Point(0,0)
        self.C = Point(AC * factor , 0)
        self.B = Point( x * factor , BD * factor)
    
    def compare(self, curva):
        return 0.6
    
    def __str__(self):

        return str(self.id) + "," + str(self.A) +"," + str(self.B) +"," + str(self.C)  + "," + str(self.t)


