with open("Day 2/in.txt","r") as file:
    for line in file:
        ranges = line.split(',')
ans = 0
for i in ranges:
    left = int(i.split('-')[0])
    right = int(i.split('-')[1])
    
    for j in range(left, right+1):
        s = str(j)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            if s[0:mid] == s[mid:]:
                ans += j
print(ans)