"""Two concrete operations expose the duplication we will refactor next."""


class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        return self.a + self.b


class Subtract:
    # These same storage steps also appear in Add. Stage 2B moves them once.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        return self.a - self.b
