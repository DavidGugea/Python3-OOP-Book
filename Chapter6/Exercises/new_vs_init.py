class A:
    def __init__(self, a, b, c):
        print("INIT")

        self.a = a
        self.b = b
        self.c = c


    def __new__(cls, *args, **kwargs):
        print("NEW")

        return object.__new__(cls)

a = A(1, 2, 3)