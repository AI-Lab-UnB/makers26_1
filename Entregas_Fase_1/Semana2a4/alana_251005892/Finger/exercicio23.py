#Q1: running_product (a) -> θ(n)
# O loop roda de 5 ate a+5, ou seja, executa exatamente a iteraçoes
# Como n=a, complexidade e θ(n).

#Q2: tricky_f(L, L2) -> θ(n²)
# Há dois loops: o de fora percorre L (n elementos) e, para cada
# elemento, verifica se está em L2(mais n elementos).
# Loop aninhado = n * n= θ(n²)

#Q3: sum_f(n) -> θ(log n)
# A cada iteração do while, n e divido por 10.
# O numero de vezes que você divide n por 10 ate chegar a 0 
# e log(n), ou seja, θ(log n)