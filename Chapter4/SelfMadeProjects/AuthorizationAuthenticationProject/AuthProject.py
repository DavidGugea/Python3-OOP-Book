import hashlib
import random

class UserNotAuthorizedForAction(Exception):
    def __init__(self, message):
        print("User AUTH Exception : {0}".format(message))

class InvalidAccount(Exception): pass
class InvalidUserAccessId(Exception) : pass

class System:
    _Users = dict()
    
    @staticmethod
    def add_user(User):
        '''Add a user to the system'''
        password_hashlib = hashlib.sha256(User.password.encode("utf-8")).hexdigest()
        System._Users.setdefault(password_hashlib, User)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self._access_id = None
        self._access_list = None
    
    def start_action(self, action):
        '''Make a user try to complete in action'''
        if action in self._access_list:
            print("User finished action {0}".format(action))
        else:
            raise UserNotAuthorizedForAction("You don't have the right to do that")

class Authenticator:
    @staticmethod
    def check_user(username, password):
        password_hashlib = hashlib.sha256(password.encode("utf-8")).hexdigest()
        password_valid = password_hashlib in System._Users.keys()

        if not password_valid:
            raise InvalidAccount

        user = System._Users.get(password_hashlib)
        user._access_id = random.choice(list(range(1, 6)))

        if user.username != username:
            raise InvalidAccount
        else:
            return Authorizor.assign_user_actionList(user)

class Authorizor:
    @staticmethod
    def assign_user_actionList(user):
        '''Assign an action list to the user depending on his access id'''
        action_dict = {
            1 : ["action_1", "action_2", "action_3", "action_4", "action_5"],
            2 : ["action_2", "action_3", "action_4", "action_5"],
            3 : ["action_3", "action_4", "action_5"],
            4 : ["action_4", "action_5"],
            5 : ["action_5"],
        }

        if user._access_id in action_dict.keys():
            user._access_list = action_dict.get(user._access_id)
        else:
            raise InvalidUserAccessId

        return user

if __name__ == "__main__":
    # Testing everything

    # Add some users inside the system
    user1 = User("username_1", "password_1")
    user2 = User("username_2", "password_2")
    user3 = User("username_3", "password_3")
    user4 = User("username_4", "password_4")
    user5 = User("username_5", "password_5")

    System.add_user(user1)
    System.add_user(user2)
    System.add_user(user3)
    System.add_user(user4)
    System.add_user(user5)

    print(System._Users)

    # Ask the user for username and password until he gets them right:
    user_found = None
    while True:
        try:
            username = input("Username : ")
            password = input("Password : ")

            user = Authenticator.check_user(username, password)
        except ( InvalidAccount, InvalidUserAccessId ):
            print("Something went wrong when trying to log you in")
        else:
            user_found = user
            break
    
    print(user_found.username)
    print(user_found.password)
    print(user_found._access_id)
    print(user_found._access_list)
    
    # Make some action with the user
    while True:
        try:
            action_to_make = input("What action would you like to make: ")
            user_found.start_action(action_to_make)
        except UserNotAuthorizedForAction:
            print("It looks like you are not allowed to make that action")
        except KeyboardInterrupt:
            break