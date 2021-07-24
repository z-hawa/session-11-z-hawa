import math


class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self, other):
        '''Checks if a polygon object is equal to the current object'''
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        '''Checks if a polygon object is greater than the current object'''
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
    def __len__(self) -> int:
        '''Returns the length of this Polygon instance'''
        return self.MaxVertice - 2  # Since Polygons with less than 3 sides do not exist
    

    def __getitem__(self, vertex):
        """This function returns the area at the specific index"""
        if isinstance(vertex, int):
            # To emulate reverse indexing
            if vertex == 0:
                vertex=self._n
            elif vertex < 1:
                vertex = vertex + self._n + 1
            else:
                vertex+=2
            if vertex < 3:
                raise IndexError("A Polygon with less than 3 sides does not exist!")
            if vertex > self._n:
                raise IndexError("A Polygon with that vertice is out of bounds!")
            else:
                return Polygon(vertex, self._R)
        else:
            idx = list(vertex.indices(self._n))
            RangeOfNumbersToGet = range(idx[0]+3, idx[1] + 3, idx[2])
            return [self[n] for n in RangeOfNumbersToGet]
    
    def __iter__(self):
        '''Function that initialises the Iteration class for the iteration'''
        return self.PolygonIters(self)
    
    class PolygonIters:
        def __init__(self, polygon_obj):
            self._polygon_obj = polygon_obj
            self._index = 3
            
        def __iter__(self):
            '''Function to initialise the iteration'''
            return self
        
        def __next__(self):
            '''Function to iterate over the polygon class'''
            if self._index >= self._polygon_obj._n:
                raise StopIteration
            else:
                item = Polygon(self._index,self._polygon_obj._R)
                self._index += 1
                return item

temp=Polygon(7,5)
for i in temp:
    print(i.area,i.perimeter)
print("iter in Polygon"," | Next in PolygonIteration")
print("__iter__" in dir(Polygon),"                      ","__next__" in dir(Polygon.PolygonIters))
