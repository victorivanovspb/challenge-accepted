# -*- coding: utf-8 -*-
"""
    Задача 3
        Легко распилить кубик 3 × 3 × 3 на 27 кубиков шестью распилами.
        Можно ли уменьшить число распилов, если разрешается перекладывать
        части перед тем как их пилить?
"""

class FragmentError(Exception):
    def __init__(self, err):
        Exception.__init__(self, err)

class Fragment(object):
    @staticmethod
    def __get_rounded_half_(value):
        if type(value) != int:
            raise TypeError("argument is not integer")
        if value < 1:
            raise ValueError("argument value cannot be less than 1") 
        h = int(round(value / 2))
        return (h, value - h)
    
    def __init__(self, x, y, z):
        if x >= 1 and y >= 1 and z >= 1:
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError("bad initial arguments: " + str(x) + "," + str(y) + "," + str(z))
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
    
   
    def __x_is_max_side_(self):
        if self.x >= self.y and self.x >= self.z:
            return True
        
    def __y_is_max_side_(self):
        if self.y >= self.x and self.y >= self.z:
            return True
    
    def __z_is_max_side_(self):
        if self.z >= self.x and self.z >= self.y:
            return True

    def is_minimal(self):
        if self.x == 1 and self.y == 1 and self.z == 1:
            return True
        return False
    
    def cut(self):
        if self.is_minimal():
            raise FragmentError("cannot cut minimal fragment (1,1,1)")
        
        nx = self.x
        ny = self.y
        nz = self.z        
        if self.__x_is_max_side_():
            self.x, nx = self.__get_rounded_half_(self.x)
        elif self.__y_is_max_side_():
            self.y, ny = self.__get_rounded_half_(self.y)
        elif self.__z_is_max_side_():
            self.z, nz = self.__get_rounded_half_(self.z)
        
        return Fragment(nx, ny, nz)


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    fragments = []
    fragments.append(Fragment(3, 3, 3))
    
    all_fragments_are_minimal = False 
    counter = 0
    while not all_fragments_are_minimal:
        counter += 1
        new_fragments = []
        
        all_fragments_are_minimal = True
        for fragment in fragments:
            if not fragment.is_minimal():
                all_fragments_are_minimal = False
                new_fragments.append(fragment.cut())
        fragments.extend(new_fragments)
        
        if all_fragments_are_minimal:
            break
        
        msg = str(counter) + " [" + str(len(fragments)) + "]: "
        for fragment in fragments:
            msg += str(fragment) + " "
        print msg

    print "All fragments are minimal (1,1,1)."
