from Property import Property

class Apartment(Property):
    def __init__(self, square_meters, number_of_bedrooms, number_of_bathrooms, price, available_purchase, available_rent, has_furniture, laundry_type, has_balcony):
        super().__init__(square_meters, number_of_bedrooms, number_of_bathrooms, price, available_purchase, available_rent, has_furniture)

        self.laundry_type = laundry_type
        self.has_balcony = has_balcony