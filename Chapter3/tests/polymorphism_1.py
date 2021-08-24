class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness
    
    def likes_walks(self):
        return True

    def method(self):
        return "default_value"

class Samoyed(Dog):
    def __init__(self, name, age, friendliness) :
        super().__init__(name, age, friendliness)

    def method(self):
        return "special sammoyed value"

class Poodle(Dog):
    def __init__(self, name, age, friendliness) :
        super().__init__(name, age, friendliness)
    
class GoldenRetriever(Dog):
    def __init__(self, name, age, friendliness) :
        super().__init__(name, age, friendliness)

    def method(self):
        return "special gr value"

sammy = Samoyed("Sammy", 2, 10)
random_dog = GoldenRetriever("random dog", 1, 10)
generic_dog = Dog("generic dog", 5, 5)

print(sammy.method())
print(random_dog.method())
print(generic_dog.method())