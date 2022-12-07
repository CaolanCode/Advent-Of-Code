# part 1
# look for four not matching characters in a string and output the position of the last position
# part 2
# look for 14 destinct characters

def part_one():
    with open("day_six.txt", 'r') as f:
        file = f.read()
        number = 0
        while number == 0:
            for c in range(len(file)-4):
                current = ""
                for i in [0,1,2,3]:
                    if file[c+i] in current:
                        break
                    else:
                        current += file[c+i]
                if len(current) == 4:
                    number = c + i + 1
                    break
    print(number)
            
def part_two():
    with open("day_six.txt", 'r') as f:
        file = f.read()
        number = 0
        while number == 0:
            for c in range(len(file)-14):
                current = file[c:c+14]
                if len(set(current)) == len(current):
                    number += c + 14
                    break
        print(number)

part_one()
part_two()
