class FourDivisionError(Exception):
    def __init__(self, m):
        self.m = m
        super().__init__(self.m)
