class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony ='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")

        print("laundry : {0}".format(self.laundry))
        print("has balcony : {0}".format(self.balcony))

        parent_init = Property.prompt_init()

        return parent_init

    def prompt_init(self):
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have", Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony", Apartment.valid_balconies)

        parent_init.update({
            "laundry" : laundry,
            "balcony" : balcony
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)

def get_valid_input(input_string, valid_options):
    input_string += "{0}".format(", ".join(valid_options))
    response = input(input_string)

    while response.lower() not in valid_options:
        reseponse = input(input_string)

    return response