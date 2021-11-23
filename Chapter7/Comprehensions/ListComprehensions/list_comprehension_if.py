values = ['1', '2', '11', '22', '111', '222', '1111', '2222']
result = {int(n) for n in values if len(n) < 3}
print(result)