from agent import Agent
from House import House
from Apartment import Apartment
from Property import Property

import sys
import distutils.util

class App():
    def run(self):
        self.agent = Agent()

        '''Start running the app. Start by asking the main questions'''
        while True:
            user_choice = self.mainQuestions()
            self.check_for_type(int, user_choice)

            if user_choice == 1:
                self.agent_add_property()
            elif user_choice == 2:
                self.agent_mark_property_sold()
            elif user_choice == 3 :
                self.agent.display_all_properties()
            elif user_choice == 4:
                self.agent_change_property_square_meters()
            elif user_choice == 5:
                self.agent_change_property_number_of_bedrooms()
            elif user_choice == 6:
                self.agent_change_property_number_of_bathrooms()
            elif user_choice == 7:
                break

            continue
    
    def check_for_type(self, wanted_type, user_input):
        try:
            if wanted_type == int:
                user_input = int(user_input)
            elif wanted_type == bool:
                user_input = distutils.util.strtobool(user_input)
            
            return user_input
        except ValueError:
            print("Your input was invalid. The type of value that we want is {0}, your input is {1}".format(
                wanted_type,
                user_input
            ))
            sys.exit(0)

    def mainQuestions(self):
        print("Choose something -- > ")
        print("1. Add a property")
        print("2. Mark a property sold")
        print("3. Display all properties")
        print("4. Change property square meters")
        print("5. Change property number of bedrooms")
        print("6. Change property number of bathrooms")
        print("7. Quit")

        user_choice = input("Choice ( 1 - 7 ) -- > ")

        try:
            user_choice = int(user_choice)
            return user_choice
        except ValueError:
            print("Your choice has to be a number between 1 and 7.")
            self.mainQuestions()

    def agent_add_property(self):
        user_property_type = input("What's the type of property that you want to add ? -- > ")
        if user_property_type not in ["House", "Apartment"]:
            print("Choose something between House and Apartment.")
            self.agent_add_property()

        square_meters = input("Square meters -- > ")
        square_meters = self.check_for_type(int, square_meters)

        number_of_bedrooms = input("Number of bedrooms -- > ")
        number_of_bedrooms = self.check_for_type(int, number_of_bedrooms)

        number_of_bathrooms = input("Number of bathrooms -- > ")
        number_of_bathrooms = self.check_for_type(int, number_of_bathrooms)

        price = input("Price :")
        price = self.check_for_type(int, price)

        available_purchase = input("Available for purchase -- > ")
        available_purchase = self.check_for_type(bool, available_purchase)

        available_rent = input("Available for rent -- > ")
        available_rent = self.check_for_type(bool, available_rent)

        has_furniture = input("Does it have furniture -- > ")
        has_furniture = self.check_for_type(bool, has_furniture)

        if user_property_type == "House":
            garden_square_meters = input("Garden square meters -- > ")
            garden_square_meters = self.check_for_type(int, garden_square_meters)

            fenced_garden = input("Fenced garden -- > ")
            fenced_garden = self.check_for_type(bool, fenced_garden)

            add_house = House(
                square_meters, number_of_bedrooms, number_of_bathrooms, price, available_purchase, available_rent, has_furniture, garden_square_meters, fenced_garden 
            )
            self.agent.add_property(add_house)
        elif user_property_type == "Apartment":
            laundry_type = input("Laundry type -- > ")

            has_balcony = input("Has balcony -- > ")
            has_balcony = self.check_for_type(bool, has_balcony)

            add_apartment = Apartment(
                square_meters, number_of_bedrooms, number_of_bathrooms, price, available_purchase, available_rent, has_furniture, laundry_type, has_balcony
            )
            self.agent.add_property(add_apartment)

    def agent_mark_property_sold(self):
        user_property_id = input("Property id -- > ")
        user_property_id = self.check_for_type(int, user_property_id)
        self.agent.mark_property_sold(user_property_id)

    def agent_change_property_square_meters(self):
        user_property_id = input("Property id -- > ")
        user_property_id = self.check_for_type(int, user_property_id)

        user_new_square_meters = input("New square meters -- > ") 
        user_new_square_meters = self.check_for_type(int, user_new_square_meters)

        self.agent.change_property_square_meters(user_new_square_meters, user_property_id)

    def agent_change_property_number_of_bedrooms(self):
        user_property_id = input("Property id -- > ")
        user_property_id = self.check_for_type(int, user_property_id)

        user_new_number_of_bedrooms = input("New number of bedrooms-- > ") 
        useR_new_number_of_bedrooms = self.check_for_type(int, user_new_number_of_bedrooms)

        self.agent.change_property_number_of_bedrooms(user_new_number_of_bedrooms, user_property_id)

    def agent_change_property_number_of_bathrooms(self):
        user_property_id = input("Property id -- > ")
        user_property_id = self.check_for_type(int, user_property_id)

        user_new_number_of_bathrooms = input("New square meters -- > ") 
        user_new_number_of_bathrooms = self.check_for_type(int, user_new_number_of_bathrooms)

        self.agent.change_property_number_of_bedrooms(user_new_number_of_bathrooms, user_property_id)

if __name__ == "__main__":
    app = App()
    app.run()