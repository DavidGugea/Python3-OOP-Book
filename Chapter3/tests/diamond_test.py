class BaseClass:
    BaseClass_calls = 0

    def call(self):
        print("Base class called.")
        BaseClass.BaseClass_calls += 1

class LeftDiamond_Subclass(BaseClass):
    LeftClass_calls = 0

    def call(self):
        super().call()

        print("Left diamond subclass called.")
        LeftDiamond_Subclass.LeftClass_calls += 1

class RightDiamond_Subclass(BaseClass):
    RigtClass_calls = 0

    def call(self):
        super().call()

        print("Right diamond subclass called.")
        RightDiamond_Subclass.RigtClass_calls += 1

class Subclass(LeftDiamond_Subclass, RightDiamond_Subclass):
    Subclass_calls = 0

    def call(self):
        print(super())
        super().call()

        print("Bottom diamond class called.")
        Subclass.Subclass_calls += 1

s = Subclass()
s.call()