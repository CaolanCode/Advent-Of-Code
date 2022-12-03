# Rearraging rucksacks
# Every item is identified by a lowercase or uppercase character
# A list of items in a rucksack is given as a line of characters
# The first half of the characters is the first compartment and the second half is the second compartment
# Find the item that appears in both compartments of the bag
# Priority for a - z: 1 - 26
# Priority for A - Z: 27 - 52
# ASCII values A - Z: 65 - 90
# ASCII values a - z: 97 - 122

def uppercase(letter):
    value = ord(letter) - 64
    return value

def lowercase(letter):
    value = ord(letter) - 96
    return value

def compare_half(first_bag_list, second_bag_list):
    item = ''
    for letter in first_bag_list:
        if letter in second_bag_list:
            item = letter
            return item

items = open("rucksack_items.txt", 'r')
total_sum = 0
all_items_list = []
first_bag_list = []
second_bag_list = []
middle_index = 0
letter = ''

for line in items:
    all_items_list = [x for x in line]
    middle_index = len(all_items_list)//2
    first_bag_list = all_items_list[:middle_index]
    second_bag_list = all_items_list[middle_index:]
    letter = compare_half(first_bag_list, second_bag_list)
    if letter.islower():
        total_sum += lowercase(letter)
    elif letter.isupper():
        total_sum += uppercase(letter)

print(f"Total sum of the priorities is: {total_sum}")
items.close()
