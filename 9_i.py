m = []

with open("in.txt", "r") as file:
    for line in file:
        x, y = map(int,line.strip().split(','))
        m.append([x,y])

max = 0

for i in range(len(m)):
    for j in range(i):
        area = (abs(m[i][0] - m[j][0]) + 1) * (abs(m[i][1] - m[j][1]) + 1)
        if area > max:
            max = area

print(max)