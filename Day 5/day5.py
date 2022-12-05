#Day 5 Part 1
with open('day5.in') as file:
    data = [i for i in file.read().replace('move ', '').replace(' from ', ',').replace(' to ', ',').strip().split('\n')]

top = []
cargo = [
    ['S', 'T', 'H', 'F', 'W', 'R'],
    ['S', 'G', 'D', 'Q', 'W'],
    ['B', 'T', 'W'],
    ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'],
    ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z'],
    ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G'],
    ['Z', 'B', 'R', 'T', 'W', 'G', 'P'],
    ['N', 'G', 'M', 'T', 'C', 'J', 'R'],
    ['L', 'G', 'B', 'W']
]
 
index = 0
length = len(data)

while index < length:
    i = 0
    procedure = data[index].split(',')
    move = int(procedure[0])
    first = int(procedure[1]) - 1
    second = int(procedure[2])- 1
    
    while i < move:
        cargo[second].append(cargo[first].pop())
        i += 1

    index += 1

x = 0
while x < len(cargo):
    top.append(cargo[x].pop())
    x += 1

print(top)