# Find the matching item in every three bags
# return the value of each item
from itertools import islice

def uppercase(letter):
    value = ord(letter) - 38
    return value

def lowercase(letter):
    value = ord(letter) - 96
    return value

def compare_half(first_bag, second_bag, third_bag):
    for letter in first_bag:
        if letter in second_bag and letter in third_bag:
            return letter

total_sum = 0

print(f"Total sum of the priorities is: {total_sum}")
