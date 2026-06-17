## Question 1: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function. Assume n = a.
```
def running_product(a):
    """ a is an int """
    product = 1
    for i in range(5,a+5):
        product *= i
        if product == a:
            return True
    return False
```

 ### Resposta: 
 $\Theta(n)$, Como assumimos n = a, o loop executa n vezes, As operações dentro do loop são de tempo constante O(1).

## Question 2: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function. Assume n = len(L).
```
def tricky_f(L, L2):
    """ L and L2 are lists of equal length """
    inL = False
    for e1 in L:
        if e1 in L2:
            inL = True
    inL2 = False
    for e2 in L2:
        if e2 in L:
            inL2 = True
    return inL and inL2
```
 ### Resposta: 
$\Theta(n^2)$, O primeiro loop percorre n elementos de L e dentro dele a operação de 'if' 'in' percorre a lista L2 para procurar elemento, tornando o primeiro bloco $n \times n = O(n^2)$.
O segundo faz exatamente o mesmo e somando os blocos independentes temos $\Theta(n^2)$.

## Question 3: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function.
```
def sum_f(n):
    """ n > 0 """
    answer = 0
    while n > 0:
        answer += n%10
        n = int(n/10)
    return answer
```
 ### Resposta: 
 $\Theta(\log n)$, Em cada interação do `while` o número n é dividido por 10.O número de vezes que podemos fazer isso é proporcional ao número de dígitos que ele tem, que é dado por $\lfloor \log_{10}(n) \rfloor + 1$.