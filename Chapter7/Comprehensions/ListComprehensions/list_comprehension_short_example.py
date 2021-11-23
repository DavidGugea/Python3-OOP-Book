input_strings = ['1', '5', '28', '131', '3']

"""
No list comprehension

output_integers = []
for num in input_strings:
    output_integers.append(int(num))
"""

# With list comprehension:
output_integers = [int(num) for num in input_strings]

print(output_integers)