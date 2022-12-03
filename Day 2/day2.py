
with open('day2.in') as file:
    games = [i for i in file.read().strip().split("\n")]

score = 0 
real_score = 0
for i in games:
    if i == "A X":
        score += 4
    elif i == "A Y":
        score += 8
    elif i == "A Z":
        score += 3
    elif i == "B X":
        score += 1
    elif i == "B Y":
        score += 5
    elif i == "B Z":
        score += 9
    elif i == "C X":
        score += 7
    elif i == "C Y":
        score += 2
    elif i == "C Z":
        score += 6

print(score)

for i in games:
    if i == "A X":
        real_score += 3
    elif i == "A Y":
        real_score += 4
    elif i == "A Z":
        real_score += 8
    elif i == "B X":
        real_score += 1
    elif i == "B Y":
        real_score += 5
    elif i == "B Z":
        real_score += 9
    elif i == "C X":
        real_score += 2
    elif i == "C Y":
        real_score += 6
    elif i == "C Z":
        real_score += 7

print(real_score)