n = int(input("Type the number that you want to calculate the cube root: (must have been a perfect cube) "));

i = 1;
while (i**3 < n):
	i += 1;

if (i**3 == n):
	print(f"The cube root of {n} is {i}.");
else:
	print(f"Error: {n} is not a perfect cube!");