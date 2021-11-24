class A:
    def print(self):
        print("My class is A")


def fake_print():
    print("My class is not A")


a = A()
a.print()
a.print = fake_print
a.print()
