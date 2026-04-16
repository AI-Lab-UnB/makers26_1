def eval_quadratic(a, b, c, x):
	return a*x*x + b*x + c;

print("Question 1:\n");
print(eval_quadratic(1, 1, 1, 1), "\n");

def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
		return (a1*x1*x1 + b1*x1 + c1) + (a2*x2*x2 + b2*x2 + c2);

print("Question 2:\n")
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1);
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1));