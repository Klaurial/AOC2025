with open("Day 2/in.txt","r") as file:
    for line in file:
        ranges = line.split(',')
ans = 0
for i in ranges:
    left = int(i.split('-')[0])
    right = int(i.split('-')[1])
    
    for j in range(left, right+1):
        s = str(j)
        
        for l in range(1,len(s) // 2 + 1):
            if len(s) % l != 0:
                continue
            flag = True
            for m in range(len(s) // l - 1):
                if s[m * l : (m+1) * l] != s[(m+1) * l : (m+2) * l]:
                    flag = False
            if flag:
                print(j)
                ans += j
                break

print(ans)