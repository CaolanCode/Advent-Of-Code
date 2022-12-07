# look for four not matching characters in a string and output the position of the last position

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
            
