# # Filling in the map using DFS.
# def fill_in(map, x, y):
#     map[x][y] = 1
#     if x>0 and map[x-1][y] == 0:
#         fill_in(map, x-1, y)
#     if y>0 and map[x][y-1] == 0:
#         fill_in(map, x, y-1)
#     if x<d-1 and map[x+1][y] == 0:
#         fill_in(map, x+1, y)
#     if y<d-1 and map[x][y+1] == 0:
#         fill_in(map, x, y+1)
#     return map

m = []
xcoords = []
ycoords = []

with open("Day 9/in.txt", "r") as file:
    for line in file:
        x, y = map(int,line.strip().split(','))
        m.append([x,y])
        xcoords.append(x)
        ycoords.append(y)

xcoords = sorted(set(xcoords))
ycoords = sorted(set(ycoords))

xlookup = [0 for i in range(100000)]
ylookup = [0 for i in range(100000)]

for i in range(len(xcoords)):
    xlookup[xcoords[i]] = 2 * i + 1
for i in range(len(ycoords)):
    ylookup[ycoords[i]] = 2 * i + 1

d = 2 * max(len(xcoords), len(ycoords)) + 5
map = [[0 for i in range(d)] for j in range(d)]
for i in range(len(m)):
    x1, y1 = xlookup[m[i][0]], ylookup[m[i][1]]
    if (i<len(m)-1):
        x2, y2 = xlookup[m[i+1][0]], ylookup[m[i+1][1]] 
    else:
        x2, y2 = xlookup[m[0][0]], ylookup[m[0][1]]

    if x1 == x2:
        for j in range(min(y1,y2), max(y1,y2)+1):
            map[x1][j] = 1
    elif y1 == y2:
        for j in range(min(x1,x2), max(x1,x2)+1):
            map[j][y1] = 1

for i in range(d):
    if sum(map[i]) == 2:
        for j in range(d):
            if map[i][j] == 1:
                x0 = i
                y0 = j+1
                break

# Filling in the map using BFS
q = [[x0, y0]]
while q:
    x, y = q[0][0], q[0][1]
    map[x][y] = 1
    q.pop(0)

    if x>0 and map[x-1][y] == 0:
        q.append([x-1,y])
    if y>0 and map[x][y-1] == 0:
        q.append([x,y-1])
    if x<d-1 and map[x+1][y] == 0:
        q.append([x+1,y])
    if y<d-1 and map[x][y+1] == 0:
        q.append([x,y+1])


max_area = 0

for i in range(len(m)):
    for j in range(i):
        x1 = xlookup[min(m[i][0], m[j][0])]
        x2 = xlookup[max(m[i][0], m[j][0])]
        y1 = ylookup[min(m[i][1], m[j][1])]
        y2 = ylookup[max(m[i][1], m[j][1])]
        flag = True
        for k in range(x1, x2+1):
            for l in range(y1, y2+1):
                if map[k][l] == 0:
                    flag = False
        if not flag:
            continue
        area = (abs(m[i][0] - m[j][0]) + 1) * (abs(m[i][1] - m[j][1]) + 1)
        if area > max_area:
            max_area = area


print(max_area)