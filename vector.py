class Vector:

    def __init__(self, x, y):
        
        self.x = x
        self.y = y

    def __add__(self, other):
        
        '''
            add Vector
        '''

        if not isinstance(other, Vector):
            return NotImplemented

        result = Vector(self.x + other.x, self.y + other.y)

        return result

    def __sub__(self, other):
        
        '''
            sub Vector
        '''

        if not isinstance(other, Vector):
            return NotImplemented

        result = Vector(self.x - other.x, self.y - other.y)

        return result

    def print_vector(self):

        print(self.x, self.y)

    def get_list(self):

        return [self.x, self.y]

    def sum(self, *args):

        return reduce(self.__add__, args)

    def scala_multiply(self, value):

        self.x = self.x * value
        self.y = self.y * value

    def dot(self, other):

        if not isinstance(other, Vector):
            return NotImplemented

        return sum([self.x * other.x, self.y * other.y])
        #return sum(self_i * other_i for self_i, other_i in zip())
        