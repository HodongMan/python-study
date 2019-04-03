

class ClothesList:

    colors  = ['black', 'white']
    sizes   = ['S', 'M', 'L']

    def __init__(self):

        self.clothes = [(color, size) for color in colors for size in sizes]