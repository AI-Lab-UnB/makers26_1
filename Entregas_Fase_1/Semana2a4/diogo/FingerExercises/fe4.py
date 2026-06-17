import math

found = False
for i in range(math.sqrt(N)):
    if(i**3 == N): 
        print(i)
        found = True
        break
    
if(found):
    print("error")