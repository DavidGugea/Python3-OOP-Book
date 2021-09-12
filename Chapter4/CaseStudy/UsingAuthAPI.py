import CaseStudy_AuthProject as auth

# Set up a test user and permission
auth.authenticator.add_user("joe", "joepassword")
auth.authorizor.add_permission("test program")
auth.authorizor.add_permission("change program")
auth.authorizor.permit_user("test program", "joe")

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login" : self.login,
            "test" : self.test,
            "change" : self.change,
            "quit" : self.quit
        }
    
    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")

            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
    
    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{0} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{0} cannot {1}".format(e.username, permission))
        else:
            return True
    
    def test(self):
        if self.is_permitted("test program"):
            print("Testing program no...")
    
    def change(self):
        if self.is_permitted("change program"):
            print("Changin program now")
    
    def quit(self):
        raise SystemExit()
    
    def menu(self):
        try:
            answer = str()
            while True:
                print("""
Please enter a command:
\tlogin\tLogin
\test\tTest the program
\change\tChange the program
\quit\tQuit the program
""")

                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{0} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")

Editor().menu()