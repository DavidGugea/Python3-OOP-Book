def decoratorMethod(methodToWrap):
    def wrapper(*args, **kwargs):
        print("Before the method")
        methodToWrap(*args, **kwargs)
        print("After the method")

    return wrapper


@decoratorMethod
def testMethod(num):
    print("Inside the method. Given argument -- > {0}".format(num))


testMethod(5)
print("-"*25)
testMethod(10)