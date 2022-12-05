
# Rearrange stacks
# given number of elements to move from one stack to another in same order
# When finished report the elements on top of the array
# Combine the elements together
Stack = [
     ['V','C','D','R','Z','G','B','W'],
 ['G','W','F','C','B','S','T','V'],
 ['C','B','S','N','W'],
 ['Q','G','M','N','J','V','C','P'],
 ['T','S','L','F','D','H','B'],
 ['J','V','T','W','M','N'],
 ['P','F','L','C','S','T','G'],
 ['B','D','Z'],
 ['M','N','Z','W']
]


file = open("day_five.txt", 'r').read().strip()
lines = [x.strip() for x in file.split('\n')]

for command in lines:
    words = command.split()
    qty = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])
    i = 0
    tempStack = []
    while i < qty:
        move = Stack[from_stack-1].pop()
        tempStack.append(move)
        i += 1
    i = 0
    while i < qty:
        move = tempStack.pop()
        Stack[to_stack-1].append(move)
        i += 1

ends = ""
for lines in Stack:
    ends = ends + lines[len(lines)-1]

print(ends)
