pos = 50
pswd = 0

with open("Day 1/in.txt", "r") as file:
    for line in file:
        rot = int(line[1:])
        if line[0] == 'L':
            pos = (pos - rot) % 100
        elif line[0] == 'R':
            pos = (pos + rot) % 100
        if pos == 0:
            pswd += 1
print(pswd)