"""
import ecommerce.database
# import ecommerce.payments.paypal

db = ecommerce.database.Database()
# paypal = ecommerce.payments.paypal.PayPal()

print("file : {0:<35} || name : {1:<20} || package : {2:<20}".format(
    str(__file__).split("\\")[-1],
    str(__name__),
    str(__package__)
))

print("-"*100)

print("file : {0:<35} || name : {1:<20} || package : {2:<20}".format(
    str(ecommerce.database.__file__).split("\\")[-1],
    str(ecommerce.database.__name__),
    str(ecommerce.database.__package__),
))
"""

class Hurensohn:
    pass