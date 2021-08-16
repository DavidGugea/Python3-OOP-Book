if __name__ == "__main__":
    import products

    x = products.Product()

class Database:
    pass

print("file : {0:<35} || name : {1:<20} || package : {2:<20}".format(
    str(__file__).split("\\")[-1],
    str(__name__),
    str(__package__),
))