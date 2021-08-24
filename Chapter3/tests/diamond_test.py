class BaseClass:
    BaseClass_calls = 0
    class_id = 1

    def call(self):
        print("Base class called.")
        BaseClass.BaseClass_calls += 1

class LeftDiamond_Subclass(BaseClass):
    LeftClass_calls = 0
    class_id = 2

    def call(self):
        # super().call()

        print("--------------------------------------------------------")
        print(super().class_id) # 3 meaning that the super() in this case is right diamond subclass
        print(super())
        print("--------------------------------------------------------")

        BaseClass.call(self)

        print("Left diamond subclass called.")
        LeftDiamond_Subclass.LeftClass_calls += 1

class RightDiamond_Subclass(BaseClass):
    RigtClass_calls = 0
    class_id = 3

    def call(self):
        # super().call()
        BaseClass.call(self)

        print("Right diamond subclass called.")
        RightDiamond_Subclass.RigtClass_calls += 1

class Subclass(LeftDiamond_Subclass, RightDiamond_Subclass):
    Subclass_calls = 0
    class_id = 4

    def call(self):

        """
        print("--------------------------------------------------------")
        print(super().class_id)
        print(super())
        print("--------------------------------------------------------")
        """    

        LeftDiamond_Subclass.call(self)
        RightDiamond_Subclass.call(self)
    
        print("Bottom diamond class called.")
        Subclass.Subclass_calls += 1

s = Subclass()
s.call()
print("---------------------------------------------------------------------------------");
print("base calls -- > {0}".format(BaseClass.BaseClass_calls))
print("left calls -- > {0}".format(LeftDiamond_Subclass.LeftClass_calls))
print("right calls -- > {0}".format(RightDiamond_Subclass.RigtClass_calls))
print("subclass calls -- > {0}".format(Subclass.Subclass_calls))