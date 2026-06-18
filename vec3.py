import numpy as np
import math

# vec3 class
class vec3():
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    
    # vector functions (for utility)
    # ----------------------------------------------------------

    def x(self):
        return self.x
    def y(self):
        return self.y
    def z(self):
        return self.z
    
    def length_squared(self):
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def length(self):
        return math.sqrt(self.length_squared())
    
    # operations

    def __add__(self, obj2):
        self.x += obj2.x
        self.y += obj2.y
        self.z += obj2.z
        return self

    def __sub__(self, obj2):
        self.x -= obj2.x
        self.y -= obj2.y
        self.z -= obj2.z
        return self

    def __mult__(self, obj2):
        temp = (self.x, self.y, self.z)
        if isinstance(obj2, vec3):
            temp[0] *= obj2.x
            temp[1] *= obj2.y
            temp[2] *= obj2.z
            return self
        
        elif isinstance(obj2, int) or isinstance(obj2, int):
            temp[0] *= obj2
            temp[1] *= obj2
            temp[2] *= obj2
            return self
    
    def __truediv__(self, obj2):
        temp = (self.x, self.y, self.z)
        if isinstance(obj2, vec3):
            x = temp[0] / obj2.x
            y = temp[1] / obj2.y
            z = temp[2] / obj2.z
            return vec3(x, y, z)
        elif isinstance(obj2, int) or isinstance(obj2, float):
            x = temp[0] / obj2
            y = temp[1] / obj2
            z = temp[2] / obj2
            return vec3(x, y, z)
        else:
            raise TypeError
    
    def __abs__(self):
        return self.length()

    def __repr__(self):
        return str([self.x, self.y, self.z])
    # dot product
    def dot(self, obj2):
        i = self.x * obj2.x
        j = self.y * obj2.y
        k = self.z * obj2.z
        return i + j + k
    
    # cross product
    def cross(self, obj2):
        i = self.y * obj2.z - self.z * obj2.y
        j = self.z * obj2.x - self.x * obj2.z
        k = self.x * obj2.y - self.y * obj2.x
        return vec3(i, j, k)
    
    def normalise(self):
        return self / self.length()

# all testing stuff goes below:
if __name__ == "__main__":
    from time import time_ns

    myvec = vec3(3, 3, 3)
    myvec2 = vec3(-1, 3.12, 7.5)

    startTime = time_ns()
    for i in range(10000000):
        myvec.normalise()
    stopTime = time_ns()
    
    finalTime = (stopTime-startTime) / 10000000
    print(finalTime)

    