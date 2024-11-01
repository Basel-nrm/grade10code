class Wall:
    '''
    A class representing a wall object
    '''
    def __init__(self, w: float, h: float) -> None:
        '''
        Class initializer 
        '''
        self.width = w
        self.height = h

    def calc_area(self) -> float:
        '''
        Class method to return the area of the wall
        '''
        return self.width * self.height