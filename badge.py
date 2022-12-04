# Find the matching item in every three bags
# return the value of each item

def uppercase(letter):
    value = ord(letter) - 38
    return value

def lowercase(letter):
    value = ord(letter) - 96
    return value

def compare_bags(first_bag, second_bag, third_bag):
    for letter in first_bag:
        if letter in second_bag and letter in third_bag:
            return letter

total_sum = 0
file = list(open("rucksack_items.txt", 'r'))

while len(file) > 0:
    first_bag = file.pop()
    second_bag = file.pop()
    third_bag = file.pop()
    letter = compare_bags(first_bag, second_bag, third_bag)
    if letter.islower():
        total_sum += lowercase(letter)
    elif letter.isupper():
        total_sum += uppercase(letter)

print(f"Total sum of the priorities is: {total_sum}")
