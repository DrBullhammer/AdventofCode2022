with open('day3.in') as file:
    data = [i for i in file.read().split('\n')]
count = 0
duplicates = []
values = {
          'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
          'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
          'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37,
          'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49,
          'X': 50, 'Y': 51, 'Z': 52
}
data_length = len(data)
while count < data_length:
    pack = data[count]
    pack_size = len(pack)
    half = int(pack_size/2)
    second = pack[half:]
    first = pack[:half]
    for element in first:
        if element in second:
            duplicates.append(element)
            break

    count += 1
total = 0

for duplicate in duplicates:
    total += values[duplicate]

print(duplicates)
print(len(duplicates))
print(total)

triplicates = []
index = 0
while index < (data_length//3):
    bag1 = data[index*3]

    bag2 = data[3*index+1]

    bag3 = data[3*index+2]

    for character in bag1:
        if character in bag2:
            if character in bag3:
                triplicates.append(character)
                break
    index += 1
group_total = 0

for triplicate in triplicates:
    group_total += values[triplicate]

print(triplicates)
print(len(triplicates))
print(group_total)


