class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name.'''
        matching_contacts = list()
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")

for c in Contact.all_contacts.search("John"):
    print(c.name)

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self.keys():
           if not longest or len(key) > len(longest):
               longest = key
           else:
               continue
        
        return longest

longkeys = LongNameDict()
longkeys["hello"] = 1
longkeys["longest yet"] = 5
longkeys["hello2"] = "world"

print(longkeys.longest_key())