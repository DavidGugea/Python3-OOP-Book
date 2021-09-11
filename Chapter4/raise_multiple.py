def division(number):
    try:
        if number == 13:
            raise ValueError("13 is not a valid number")
        
        return 100 / number
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError as e:
        print("Not 13")