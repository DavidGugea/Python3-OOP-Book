class Context:
    def __init__(self):
        self.current_state = None

    def process(self):
        print("Processing ... ")
        self.current_state = FirstState("First state").process(self)

class BaseStateClass:
    def __init__(self, state):
        self.state = state


class FirstState(BaseStateClass):
    def process(self, manager):
        print("You are inside the first state. We are going to change to the second state")
        manager.current_state = SecondState("Second state").process(manager)


class SecondState(BaseStateClass):
    def process(self, manager):
        print("You are inside the second state. We are going to change to the third state")
        manager.current_state = ThirdState("Third state").process(manager)


class ThirdState(BaseStateClass):
    def process(self, manager):
        print("You are inside the first state. We will stop the cycle")
        manager.current_state = None


if __name__ == '__main__':
    Context().process()