from Property import Property

class House(Property):
    def __init__(self, square_meters, number_of_bedrooms, number_of_bathrooms, price, available_purchase, available_rent, has_furniture, garden_square_meters, fenced_garden):
        super().__init__(square_meters, number_of_bedrooms, number_of_bathrooms, price, available_purchase, available_rent, has_furniture)

        self.garden_square_meters = garden_square_meters
        self.fenced_garden = fenced_garden