from collections import defaultdict

def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1

    return frequencies

def letter_frequency_defaultdict(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    
    return frequencies

print(letter_frequency_defaultdict("aabbccdd"))