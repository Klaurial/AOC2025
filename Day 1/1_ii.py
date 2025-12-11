pos = 50
pswd = 0

with open("Day 1/in.txt", "r") as file:
    for line in file:
        rot = int(line[1:])
        if line[0] == 'L':
            pos -= rot
            if pos <= 0:
                pswd += (-pos) // 100 + 1
                if pos+rot == 0:
                    pswd -= 1
        elif line[0] == 'R':
            pos += rot
            if pos >= 100:
                pswd += (pos) // 100
        
        pos %= 100

print(pswd)