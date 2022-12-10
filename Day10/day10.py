with open('day10.in') as file:
    data = [i for i in file.read().split('\n')]

cycle_value = {}
value = 1
cycle = 1

for i in data:
    operation = i[:4]
    cycle_value[cycle] = value
    if operation == "noop":
        cycle += 1
        
    else:
        cycle += 1
        cycle_value[cycle] = value
        cycle += 1
        value = value + int(i[5:len(i)])

signal_strengths = (cycle_value[20] *20) + (cycle_value[60] * 60) + (cycle_value[100] * 100) + (cycle_value[140] * 140) + (cycle_value[180] * 180) + (cycle_value[220] * 220)
print(signal_strengths)

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []

row_out1 = ''
row_out2 = ''
row_out3 = ''
row_out4 = ''
row_out5 = ''
row_out6 = ''

x = 0
while x < len(cycle_value):
    if x < 40:
        row1.append(cycle_value[x+1])
    if 40 <= x <80:
        row2.append(cycle_value[x+1])
    if 80 <= x < 120:
        row3.append(cycle_value[x+1])
    if 120 <= x < 160:
        row4.append(cycle_value[x+1])
    if 160 <= x < 200:
        row5.append(cycle_value[x+1])
    if 200 <= x < 240:
        row6.append(cycle_value[x+1])
    x += 1

a = 0
while a < 40:
    if a-1 <= row1[a] <= a+1:
        row_out1 += '#'
    else:
        row_out1 += '.'
    a += 1

b = 0
while b < 40:
    if b-1 <= row2[b] <= b+1:
        row_out2 += '#'
    else:
        row_out2 += '.'
    b += 1

c = 0
while c < 40:
    if c-1 <= row3[c] <= c+1:
        row_out3 += '#'
    else:
        row_out3 += '.'
    c += 1

d = 0
while d < 40:
    if d-1 <= row4[d] <= d+1:
        row_out4 += '#'
    else:
        row_out4 += '.'
    d += 1

e = 0
while e < 40:
    if e-1 <= row5[e] <= e+1:
        row_out5 += '#'
    else:
        row_out5 += '.'
    e += 1

f = 0
while f < 40:
    if f-1 <= row6[f] <= f+1:
        row_out6 += '#'
    else:
        row_out6 += '.'
    f += 1

print(row_out1)
print(row_out2)
print(row_out3)
print(row_out4)
print(row_out5)
print(row_out6)