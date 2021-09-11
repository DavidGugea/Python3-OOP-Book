def division(number):
    try:
        return 100 / number
    except ZeroDivisionError:
        return "You can't devide by zero."

print(division(0))
print(division(50))
print(division("This will raise a type error since we divide by 100. It will not be handled by the ZeroDivisionError"))