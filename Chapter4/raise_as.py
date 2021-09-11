try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were {0}".format(e.args))