def eval_quadratics():
    a,b,c,x = map(int,input().split())
    return a*x*x + b*x + c

def two_quadratics():
    a,b,c,x,a1,b1,c1,x1 = map(int,input().split())
    return (a*x*x + b*x + c*x)+(a1*x1*x1+b1*x1+c1)

