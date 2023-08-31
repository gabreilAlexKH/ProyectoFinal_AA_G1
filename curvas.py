from shapely.geometry import Point
from shapely.geometry import LineString
import numpy as np

Bezier = lambda A,B,C,t: Point(((1-t)**2)*A.x + (2*(1-t)*t)*B.x + (t**2)*C.x,((1-t)**2)*A.y + (2*(1-t)*t)*B.y + (t**2)*C.y)


def proyection( A ,  B ,  P):

    if(A.x == B.x):
        line = LineString([(A.x , -100), (A.x, 100)]) 
        dist = line.project(P)
        return list(line.interpolate(dist).coords)[0]
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
        return similitud(self, curva)
    

    def copy(self):
        return Curva(self.id, self.A, self.B, self.C, self.t)
    def __str__(self):
        return str(self.id) + "," + str(self.A) +"," + str(self.B) +"," + str(self.C)  + "," + str(self.t)


def similitud(curva1, curva2):
        # Calcular las curvaturas para 'curva1' y 'curva2'
        curvatura_self = calculate_curvature(curva1)
        curvatura_curva = calculate_curvature(curva2)
        
        # Normalizar las curvaturas
        max_curvatura = max(curvatura_self, curvatura_curva)
        curvatura_self /= max_curvatura
        curvatura_curva /= max_curvatura
        
        # Calcular la diferencia en curvaturas normalizadas
        diferencia_curvatura = abs(curvatura_self - curvatura_curva)
        
        # Calcular el puntaje de similitud en función de la diferencia en curvaturas
        puntaje_similitud = 1 - diferencia_curvatura
        
        # Asegurarse de que el puntaje de similitud esté entre 0 y 1
        puntaje_similitud = max(0, min(puntaje_similitud, 1))
        
        return puntaje_similitud
    
def calculate_curvature(curva):
    # Calcular la curvatura utilizando derivadas
    t_values = np.linspace(0, 1, num=100)
    x_prime = np.gradient([curva.B.x * (1 - t)**2 + 2 * curva.C.x * t * (1 - t) + curva.A.x * t**2 for t in t_values])
    y_prime = np.gradient([curva.B.y * (1 - t)**2 + 2 * curva.C.y * t * (1 - t) + curva.A.y * t**2 for t in t_values])
    
    x_double_prime = np.gradient(x_prime)
    y_double_prime = np.gradient(y_prime)
    
    curvature = np.abs(x_prime * y_double_prime - y_prime * x_double_prime) / (x_prime**2 + y_prime**2)**(3/2)
    
    return max(curvature)

curva1 = Curva(1, Point(-2,3), Point(1,4), Point(-2,12), .4)
curva2 = Curva(2, Point(0,13), Point(11,2), Point(0,15), .6)
curva1.normalize()
curva2.normalize()

print(similitud(curva1, curva2))