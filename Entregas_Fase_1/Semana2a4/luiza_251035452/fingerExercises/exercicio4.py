n= int(input("Enter a number: "))
i=1
while n >= i**3:
     i+=1
     if i**3 == n:
         print(i)
         break   
else:
    print("error: The number is not a perfect cube  ")