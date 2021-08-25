class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return dict
    
    prompt_init = staticmethod(prompt_init)