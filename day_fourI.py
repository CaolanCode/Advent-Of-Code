# Given two ranges of numbers, return how many are fully included in their partners

with open("day_four.txt", 'r') as file:
    all_pairs = file.read().strip()

all_pairs = all_pairs.split('\n')
total_contained = 0
for pair in all_pairs:
    elf_one, elf_two = pair.split(',')
    elf_one_start, elf_one_end = map(int, elf_one.split('-'))
    elf_two_start, elf_two_end = map(int, elf_two.split('-'))
    if(elf_one_start <= elf_two_start and elf_one_end >= elf_two_end) or (elf_two_start <= elf_one_start and elf_two_end >= elf_one_end):
        total_contained += 1

print(f"Total number of pairs fully included: {total_contained}")