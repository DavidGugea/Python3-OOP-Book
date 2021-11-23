def made_range(stop, start=0, step=1):
    counter = start
    while (counter < stop):
        yield counter
        counter += step


nums = (l for l in made_range(123456789, step=100000))
for i in nums:
    print(i)
