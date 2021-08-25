class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)

        self.furnished= furnished
        self.rent = rent
        self.utilities = utilities
    
    def display(self):
        super().display()

        print("RENTAL DETAILS")
        print("rent : {0}".format(self.rent))
        print("estimated utilities : {0}".format(self.utilities))
        print("furnished : {0}".format(self.furnished))

    def prompt_init():
        return dict(
            rent = input("What is the monthly rent ?"),
            utilities = input("What are the estmiated utilities ? "),
            furnished = get_valid_input("Is the property furnished?", ("yes", "no"))
        )

    prompt_init = staticmethod(prompt_init)