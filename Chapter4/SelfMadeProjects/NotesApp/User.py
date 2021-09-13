import hashlib

class User:
    def __init__(self, firstName, lastName, username, password, premiumUser):
        self.firstName = firstName
        self.lastname = lastName 
        self.username = username
        self.password = password.encode("utf-8")
        self.premium_user = premiumUser
    
    def get_hashed_pass(self):
        '''Return the hexdigest of hashed [ sha256 ] (self.)password '''
        return hashlib.sha256(self.password).hexdigest()