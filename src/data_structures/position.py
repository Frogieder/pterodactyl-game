class Position:
    """Stores information about position of an object

    Attributes:
        x: int | float
        y: int | float

    Methods:
        from_touple(tup: tuple):
            constructs Positon from a tuple
        get():
            returns itself as a tuple
    """
    def __init__(self, x: int | float, y: int | float):
        self.x: int | float = x
        self.y: int | float = y

    @classmethod
    def from_touple(cls, tup: tuple):
        """Constructs a Position from 2-tuple (x, y)"""
        return cls(*tup)

    def get(self):
        return self.x, self.y
