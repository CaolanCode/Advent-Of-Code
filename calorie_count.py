# Discover which ELve is carrying the most calories
# Read a webpage with numbers
# The Elves calories are seperated by a blank space
# Find the Elf carrying the most calories
most_calories = 0 
current_elf = 0
calories_file = open("calories.txt", 'r')

for line in calories_file:
    if line.strip():
        current_elf += int(line.strip())
    else:
        if current_elf > most_calories:
            most_calories = current_elf
        current_elf = 0

print("The most calories is: " + str(most_calories))
calories_file.close()