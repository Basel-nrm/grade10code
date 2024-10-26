class Wall:
    def __init__(self, w: float, h: float) -> None:
        self.width = w
        self.height = h

    def calc_area(self) -> float:
        return self.width * self.height