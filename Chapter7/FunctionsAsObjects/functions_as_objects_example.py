def first_function():
    print("The first function was called")


first_function.description = "This is the first function"


def second_function():
    print("The second function was called")


second_function.description = "This is the second function"


def third_function(function):
    print("The description of the function -- > {0}".format(function.description))
    print("The name of the function -- > {0}".format(function.__name__))
    print("The class of the function -- > {0}".format(function.__class__))
    print("Calling the passed in function:")
    function()


third_function(first_function)
print("-" * 25)
third_function(second_function)
