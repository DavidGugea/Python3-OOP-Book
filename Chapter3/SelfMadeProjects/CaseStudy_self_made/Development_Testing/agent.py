from Property import Property
from House import House
from Apartment import Apartment
import logging

class Agent:
    '''The agent class.'''

    def __init__(self):
        '''The agent class contains a dictionary with all the id's of the properties as keys and the properties themselves. On top of that we keep track of the last id so we don't have to always search for it when we insert something in the dictionary since the keys have to be unique in every dictionary.'''
        self._properties_dict = dict()
        self._last_id = None;
    
    def check_property_id(self, property_id):
        '''Check the given id to make sure that it's of type int and inside the dict keys.'''
        if self._last_id <= property_id or property_id <= 0 or type(property_id) != int:
            raise ValueError("The given id is invalid.")

    def add_property(self, property_to_add):
        '''Add a new property'''
        if self._last_id == None:
            self._last_id = 1

        self._properties_dict.setdefault(self._last_id, property_to_add)
        self._last_id += 1

    def mark_property_sold(self, property_id):
        '''Mark a property sold. The property id argument is checked inside the method'''
        self.check_property_id(property_id)
        self._properties_dict.pop(property_id)
    
    def display_all_properties(self):
        '''Display all properties inside the properties dict'''

        for i in range(3):
            print()

        for property_item in self._properties_dict.items():
            print("-"*25)
            print("ID : {0}".format(property_item[0]))

            property = property_item[1]
            property_type = type(property_item)

            print("Square meters : {0}".format(property.square_meters))
            print("Number of bedrooms : {0}".format(property.number_of_bedrooms))
            print("Number of bathrooms : {0}".format(property.number_of_bathrooms))
            print("Price of property : {0}".format(property.price))
            print("Available for purchase : {0}".format(property.available_purchase))
            print("Available for rent : {0}".format(property.available_rent))
            print("Propety has furniture : {0}".format(property.has_furniture))

            if property_type == House:
                print("Graden square meters : {0}".format(property.garden_square_meters))
                print("Fenced garden : {0}".format(property.fenced_garden))
            elif property_type == Apartment:
                print("Laundry type : {0}".format(property.laundry_type))
                print("Has balcony : {0}".format(property.has_balcony))
            print("-"*25)
            print()

        for i in range(3):
            print()
    
    def change_property_square_meters(self, new_square_meters, property_id):
        '''Change the property square meters. The property id is checked inside the method.'''
        self.check_property_id(property_id)
        self._properties_dict[property_id].square_meters = new_square_meters
    
    def change_property_number_of_bedrooms(self, new_number_of_bedrooms, property_id):
        '''Change the property number of bedrooms. The property id is checked inside the method.'''
        self.check_property_id(property_id)
        self._properties_dict[property_id].number_of_bedrooms = new_number_of_bedrooms
    
    def change_property_number_of_bathrooms(self, new_number_of_bathrooms, property_id):
        '''Change the property number of bathrooms. The property id is checked inside the method.'''
        self.check_property_id(property_id)
        self._properties_dict[property_id].number_of_bathrooms = new_number_of_bathrooms

if __name__ == "__main__":
    # Make sure the agent class works
    x = Agent()
    house_1 = House(
        400,
        2,
        2,
        500000,
        True,
        False,
        True,
        50,
        True 
    )
    x.add_property(house_1)

    house_2 = House(
        1000,
        4,
        3,
        1000000,
        False,
        True,
        False,
        250,
        False 
    )
    x.add_property(house_2)

    apartment_1 = Apartment(
        250,
        2,
        1,
        250000,
        True,
        True,
        True,
        "en-suite",
        False
    )
    x.add_property(apartment_1)

    apartment_2 = Apartment(
        450,
        3,
        2,
        750000,
        False,
        False,
        False,
        "en-suite",
        True
    )
    x.add_property(apartment_2)

    x.change_property_number_of_bathrooms(3, 2)
    x.change_property_number_of_bedrooms(5, 3)
    x.change_property_square_meters(500, 4)

    x.display_all_properties()