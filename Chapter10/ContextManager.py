class TestClass:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print("Test enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Test exit")
        super().__init__()


if __name__ == '__main__':
    with TestClass(5) as test_class:
        print(test_class.value)
