def keys_with_value(adict, target):
    los=[]
    for i,k in adict.items():
        if k == target:
            los.append(i)
        
    new = sorted(los)       
    return new
adict = {1:3, 4:5, 2:9, 5:7, 5:3, 3:5, 4:3}
target = int(input("Digite o alvo "))
print(keys_with_value(adict, target))