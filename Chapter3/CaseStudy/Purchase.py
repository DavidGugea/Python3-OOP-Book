class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        
        self.price = price
        self.taxes = taxes
    
    def display(self):
        super().display()

        print("PURCHASE DETAILS")
        print("sellling price : {0}".format(self.price))
        print("estimated taxes : {0}".format(self.taxes))
    
    def prompt_init():
        return dict(
            price = input("What is the selling price ?"),
            taxes = input("What are the estimated taxes ?")
        )
    
    prompt_init = staticmethod(prompt_init)