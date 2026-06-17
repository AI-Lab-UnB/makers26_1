n = int(input("Type the number between 0 and 1000: "));
if not(-1 < n < 1001): print(f"Error, the number {n} is not between 0 and 1000!");

if (-1 < n < 1001):
	low = 0;
	high = 1001;

	guess = (low + high) // 2;
	count = 1;

	while (guess != n):
		if (guess < n):
			low = guess;
		elif(guess > n):
			high = guess;
		guess = (low + high) // 2;
		count += 1;
	print("Count of attempts: ", count);
	print("Answer: ", guess);