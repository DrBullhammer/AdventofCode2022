
with open('day4.in') as file:
    pairs = [i for i in file.read().split('\n')]

full_range_pair = 0
overlap = 0
pair_one_low = 0
pair_one_high = 0
pair_two_low = 0
pair_two_high = 0
length = len(pairs)
count = 0

#split each line into a pair of strings
while count < length:
    pair_split = pairs[count].replace('-', ',').split(',')
    pair_one_low = int(pair_split[0])
    pair_one_high = int(pair_split[1])
    pair_two_low = int(pair_split[2])
    pair_two_high = int(pair_split[3])
    
#comparisons
    if (pair_one_low <= pair_two_low and pair_one_high >= pair_two_high) or (pair_two_low <= pair_one_low and pair_two_high >= pair_one_high):
        full_range_pair +=1
        overlap += 1
    
    elif pair_one_low == pair_two_low or pair_one_high == pair_two_low or pair_one_high == pair_two_high or pair_one_low == pair_two_high:
        overlap += 1
    
    elif pair_one_low < pair_two_low and pair_one_high > pair_two_low or pair_one_low > pair_two_low and pair_one_low < pair_two_high:
        overlap += 1

    count += 1

print(full_range_pair)
print(overlap)