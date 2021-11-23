nums = (str(hex(l)) for l in range(1, 10000000001) if l < 123456789)

for i in nums:
    print(i)