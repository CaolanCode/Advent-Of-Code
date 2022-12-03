# find the top three elves carrying the most calories and return the sum

first_elf = 0 
second_elf = 0 
third_elf = 0 
current_elf = 0
total_calories = 0
calories_file = open("calories.txt", 'r')

for line in calories_file:
    if line.strip():
        current_elf += int(line.strip())
    else:
        if current_elf > first_elf:
            third_elf = second_elf
            second_elf = first_elf
            first_elf = current_elf
        elif current_elf > second_elf:
            third_elf = second_elf
            second_elf = current_elf
        elif current_elf > third_elf:
            third_elf = current_elf
        current_elf = 0

total_calories = first_elf + second_elf + third_elf
print("Top three elves are carrying: " + str(total_calories))
calories_file.close()
