import weakref
import gc
import logging


def get_stream_logger():
    handler = logging.StreamHandler()
    fmt = logging.Formatter(
        fmt="{lineno} -- > {message}",
        style="{"
    )
    handler.setFormatter(fmt)

    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger


stream_logger = get_stream_logger()


class CarModel:
    _models = weakref.WeakValueDictionary();

    def __new__(cls, model_name, *args, **kwargs):
        # Flyweight factory is implemented using the __new__ constructor
        # print("GOT INTO THE __new__ CONSTRUCTOR")
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model

        stream_logger.info("[ {0}, {1} ]".format(model, model_name))
        return model

    def __init__(self, model_name, air=False, tilt=False, cruise_control=False, power_locks=False, alloy_wheels=False,
                 usb_charger=False):
        # print("GOT INTO THE __init__ CONSTRUCTOR")
        if not hasattr(self, "initted"):
            # print("USING INIT BECAUSE THE VALUE HASN'T BEEN INITTED YET")
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
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
    dx = CarModel("FIT DX")
    lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
    lx2 = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)

    # print(id(lx))
    # print(id(lx2))

    for i in range(3):
        print()

    print("-" * 75)
    for item in CarModel._models.items():
        model_name, model = item
        """
        print("model name -- > {0}".format(model_name))
        print("model")
        print(model)
        print(model.air)
        print("-"*25)
        """

    print("-" * 75)

    """
    car1 = Car(dx, "blue", "12345")
    car2 = Car(dx, "black", "12346")
    car3 = Car(lx, "red", "12347")
    """
