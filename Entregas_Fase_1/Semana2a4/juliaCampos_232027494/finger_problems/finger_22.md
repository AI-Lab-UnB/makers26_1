## Answers

### Question 1: Simplify `n*n + log(n) + 2**a` to determine θ in terms of n.

$\Theta(2^n)$ , o exponencial $2^n$  cresce muito mais rápido que o quadrático ou logarítmico

### Question 2: Simplify `2**n + n*log(n) + n**2` to determine θ in terms of n.

$\Theta(2^n)$ Novamente a funçãodomina tanto a quadrática quanto a linear logarítmica

### Question 3: Simplify `f*log(f) + 100000 + 300*a + x*y*z` to determine θ in terms of n.

$\Theta(f \log f)$ nessa expressão o termo que depende de `f` crescendo ao infinito é $f \log f$, todos os outross são mais como constantes em relação ao crescimento de `f`.