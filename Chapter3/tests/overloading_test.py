class Test:
    def method(self, value):
        return value + 5
    
    def method(self, value1, value2):
        return value + value2

t = Test()
print(t.method(5))
print(t.method(5, 10))

# Method overloading doesn't work in python