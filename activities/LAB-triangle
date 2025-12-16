"""Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is what we want:

the constructor accepts three arguments – all of them are objects of the Point class;
the points are stored inside the object as a private list;
the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is the sum of all the lengths of the legs (we mention this for the record, although we are sure that you know it perfectly yourself.)"""

import math

class Point: 
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = float(x)
        self.__y = float(y)
    
    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y 
    
    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point): 
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3): #recebe 3 instancias de Point, mas nao herda a classe
        # armazena em um atributo privado - Triangle pode usar as funcionalidades de Point sem herdar as propriedades
        self.__vertices = [vertice1, vertice2, vertice3]
    
    def perimeter(self): #soma das 3 dsitancias
        # print(getattr(self.__vertices[1], '_Point__x'))
        # Triangle acessa os metodos de Point pelos objetos da lista
        # o 'self' do metodo Point é o objeto da lista Triangle
        # Triangle acessa os dados pelos metodos publicos (gets) - mantem encapsulamento
        return (self.__vertices[0].distance_from_point(self.__vertices[1]) +
                self.__vertices[1].distance_from_point(self.__vertices[2]) +
                self.__vertices[2].distance_from_point(self.__vertices[0]))

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    