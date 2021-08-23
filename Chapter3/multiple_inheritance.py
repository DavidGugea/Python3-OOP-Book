class Contact:
    all_contacts = list()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class MailSender:
    def send_email(self, message):
        print("Sending email to {0}".format(self.email))

        # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    pass

e = EmailableContact("John Smith", "jsmith@example.net")
print(Contact.all_contacts)
e.send_email("Hello, test e-mail here")