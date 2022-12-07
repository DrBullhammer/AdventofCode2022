with open('day6.txt') as file:
    data = [i for i in file.read()]


for i in range(len(data)):
    if i-3 >= 0 and len(set([data[i-x] for x in range(4)])) == 4:
        print(i+1)
        break

for i in range(len(data)):
    if i-13 >= 0 and len(set([data[i-x] for x in range(14)])) == 14:
        print(i+1)
        break