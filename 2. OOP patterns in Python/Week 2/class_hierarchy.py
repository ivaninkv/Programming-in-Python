import pygame
import random
import math
# from contracts import contract


SCREEN_DIM = (1024, 768)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _mul(self, k):  # умножение вектора на число
        return self.x * k, self.y * k

    def _scal_mul(self, obj):  # скалярное умножение векторов
        return self.x * obj.x, self.y * obj.y

    def __add__(self, obj):
        return self.x + obj.x, self.y + obj.y

    def __sub__(self, obj):
        return self.x - obj.x, self.y - obj.y

    def __mul__(self, obj):
        if isinstance(obj, Vec2d):
            return self._scal_mul(obj)
        else:
            return self._mul(obj)

    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        return (random.random() * 2, random.random() * 2)


class Polyline:
    def add_point(self, point):
        pass
        
    def set_points(self):
        pass

    def draw_points(self):
        pass


class Knot(Polyline):
    def get_knot(self):
        pass


 
def main():
    v1 = Vec2d(1, 2)
    v2 = Vec2d(5, 4)
    print(v1*2)
    print(v1*v2)

if __name__ == '__main__':
    main()