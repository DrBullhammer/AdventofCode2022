
with open('day1.in') as file:
    data = [i for i in file.read().strip().split("\n")]

print(data)

max_cals = 0
count = 0
elf1 = 0
elf2 = 0
elf3 = 0
top_3_elves = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > max_cals:
        max_cals = count
#added for part 2
    if count > elf1:
            elf1 = count
    elif count > elf2:
            elf2 = count
    elif count > elf3:
            elf3 = count

print("The most calories being carried is: ", max_cals)

top_3_elves = elf1 + elf2 + elf3

print("The calories carried by the top 3 elves is:  ", top_3_elves)