# Takes a long time -- > numbers = list(range(1, 100000001))
numbers = (i for i in range(1, 100000001))  # Instant
for i in numbers:
    print(i)
