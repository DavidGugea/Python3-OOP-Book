def division(number):
    try:
        if number == 13:
            raise ValueError("13 is not a valid number")
        
        return 100 / number
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than 0"

for val in (0, "hello", 50.0, 13):
    print("Testing {0}".format(val), end=" -- > ")
    print(division(val))