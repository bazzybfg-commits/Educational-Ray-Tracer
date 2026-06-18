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

    def __add__(self, other):
        if isinstance(other, vec3):
            i = self.x + other.x
            j = self.y + other.y
            k = self.z + other.z
            return vec3(i, j, k)
        else:
            raise TypeError(f"expected a vec3, got {type(other).__name__}")

    def __sub__(self, other):
        if isinstance(other, vec3):
            i = self.x - other.x
            j = self.y - other.y
            k = self.z - other.z
            return vec3(i, j, k)
        else:
            raise TypeError(f"expected a vec3, got {type(other).__name__}")

    def __mul__(self, other):
        if isinstance(other, vec3):
            return vec3(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z
            )
        
        elif isinstance(other, int) or isinstance(other, float):
            return vec3(
                self.x * other,
                self.y * other,
                self.z * other
            )
        else:
            raise TypeError
    
    def __rmul__(self, other):
        return self.__mul__(other)
            
    def __truediv__(self, other):
        if isinstance(other, vec3):
            i = self.x / other.x
            j = self.y / other.y
            k = self.z / other.z
            return vec3(i, j, k)
        
        elif isinstance(other, int) or isinstance(other, float):
            i = self.x / other
            j = self.y / other
            k = self.z / other
            return vec3(i, j, k)
        else:
            raise TypeError(f"expected vec3 or number, not {type(other).__name__}")
    
    def __rtruediv__(self, other):
        if not isinstance(other, vec3):
            raise TypeError(f"cannot divide a(n) {type(other).__name__} by a vec3")
        
    def __abs__(self):
        return self.length()

    def __repr__(self):
        return str([self.x, self.y, self.z])
    # dot product
    def dot(self, other):
        i = self.x * other.x
        j = self.y * other.y
        k = self.z * other.z
        return i + j + k
    
    # cross product
    def cross(self, other):
        i = self.y * other.z - self.z * other.y
        j = self.z * other.x - self.x * other.z
        k = self.x * other.y - self.y * other.x
        return vec3(i, j, k)
    
    def normalise(self):
        return self / self.length()

# all testing stuff goes below:
if __name__ == "__main__":
    pass
    