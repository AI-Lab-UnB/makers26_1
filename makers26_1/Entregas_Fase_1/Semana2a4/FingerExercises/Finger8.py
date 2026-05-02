def same_chars(str1,str2):
    isPresent=False
    for i in str1:
        if i in str2:
            isPresent=True

    for i in str2:
        if i in str1:
            isPresent=True

    return isPresent

str1,str2 = map(str,input().split())

if same_chars(str1,str2):
    print("Yes")
else:
    print("No")