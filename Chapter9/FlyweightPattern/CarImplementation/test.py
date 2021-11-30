class CarModel:
    _models = {}  # { model_name : model object }

    def __new__(cls, model_name, *args, **kwargs):
        # Flyweight Factory for car models
        if model_name in cls._models.keys():
            print("RETURN CACHED CAR MODEL FROM __new__")
            return cls._models[model_name]
        else:
            print("BUILD NEW CAR MODEL AND CACHE IT IN __new__")
            model = super().__new__(cls)
            print(id(model))
            cls._models[model_name] = model

        return model

    def __init__(self, model_name, property_1=False, property_2=False, property_3=False, property_4=False,
                 property_5=False):
        print("__inited__ 1")
        if not hasattr(self, "innited"):
            print("__inited__ 2")
            self.model_name = model_name
            self.property_1 = property_1
            self.property_2 = property_2
            self.property_3 = property_3
            self.property_4 = property_4
            self.property_5 = property_5
            self.innited = True

    def check_serial(self, serial_number):
        print("Sorry, we are unable to check the serial number {0} int the {1} at this time".format(
            serial_number, self.model_name
        ))


class Car:
    def __init__(self, model, color, serial):
        self.model = model
        self.color = color
        self.serial = serial

    def check_serial(self):
        return self.model.check_serial(self.serial)


if __name__ == '__main__':
    dx_all_false = CarModel("FIT DX")
    print("-"*25)
    lx_1_3 = CarModel("FIT LX", property_1=True, property_3=True)
    print("-"*25)

    for item in CarModel._models.items():
        model_name, model = item
        print("model name -- > {0}".format(model_name))
        print("model -- > {0}".format(model))
        print("model id -- > {0}".format(id(model)))
        print("model property 1 -- > {0}".format(model.property_1))
        print("model property 2 -- > {0}".format(model.property_2))
        print("model property 3 -- > {0}".format(model.property_3))
        print("model property 4 -- > {0}".format(model.property_4))
        print("-"*25)
