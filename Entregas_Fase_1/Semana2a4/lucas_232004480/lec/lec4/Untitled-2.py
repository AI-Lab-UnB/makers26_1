s = "abca"

a = ""
c = 0
for l in s:
    if l not in a:
        a += l
        c += 1
print(a,c)