class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        print("You are setting the value to {0}".format(name))
        self._name = name

    def _get_name(self):
        print("You are trying to get the value")
        return self._name

    # Set up the getter & setter for the _name property
    name = property(_get_name, _set_name)

c = Color("#0000ff", "bright red")
print(c.name)
c.name = "red"
print(c.name)
c.name = None
print(c.name)