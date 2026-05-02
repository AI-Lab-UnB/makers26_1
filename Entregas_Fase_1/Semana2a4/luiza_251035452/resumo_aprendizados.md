# Resumo: Introdução à Computação e Python

##  Fundamentos da Computação

Computação é sobre resolver problemas de forma sistemática. Os temas centrais são escrever programas modulares (divididos em partes reutilizáveis), entender algoritmos simples e analisar sua complexidade — ou seja, quão rápido ou lento um programa fica conforme a entrada cresce.

---

##  Strings, Input/Output e Condicionais

Strings são sequências de caracteres. Você pode pedir dados ao usuário com `input()`, exibir resultados com `print()`, e tomar decisões com `if`, `elif` e `else`.

---

##  Loops

Dois mecanismos principais de repetição:

**`while`** — repete enquanto uma condição for verdadeira. Cuidado com loops infinitos — a condição precisa eventualmente se tornar falsa.

**`for`** — percorre uma sequência (string, lista, range) item por item. Mais seguro e previsível que o `while`.

---

##  Floats e Métodos de Aproximação

Números de ponto flutuante (`float`) têm limitações de precisão. Para encontrar raízes ou valores aproximados, usamos métodos como tentativa e erro sistemático — testando valores até chegar perto o suficiente da resposta.

---

##  Busca por Bisseção

Em vez de testar valores um por um, a bisseção corta o intervalo de busca pela metade a cada passo. Isso torna a busca muito mais rápida — O(log n) em vez de O(n).

---

##  Decomposição, Abstração e Funções

Funções permitem dividir um problema grande em partes menores e reutilizáveis. Abstração significa que você usa uma função sem precisar saber como ela funciona por dentro — só o que ela recebe e retorna.

---

##  Funções como Objetos

Em Python, funções são objetos como qualquer outro — podem ser passadas como argumento, retornadas por outras funções e atribuídas a variáveis. **Lambda** cria funções anônimas simples em uma linha:

```python
dobro = lambda x: x * 2
```

---

##  Tuplas e Listas

**Tuplas** — sequências imutáveis: `(1, 2, 3)`. Não podem ser alteradas após criadas.

**Listas** — sequências mutáveis: `[1, 2, 3]`. Podem ser modificadas, têm métodos como `.append()`, `.remove()`, `.sort()`.

---

##  Mutabilidade, Aliasing e Clonagem

Esse é um dos pontos mais importantes e fonte de bugs:

**Mutabilidade** — listas podem ser alteradas no lugar. Strings e tuplas não.

**Aliasing** — quando duas variáveis apontam para a mesma lista, alterar uma altera a outra também:

```python
a = [1, 2, 3]
b = a        # b e a são a mesma lista
b.append(4)
print(a)     # [1, 2, 3, 4] — a também mudou!
```

**Clonagem** — para evitar isso, faça uma cópia:

```python
b = a[:]     # ou list(a)
```

---

##  Copiando Listas

Três formas de clonar uma lista para evitar aliasing:

```python
a = [1, 2, 3]
b = a[:]        # slicing
c = list(a)     # construtor
d = a.copy()    # método
```

Todas criam cópias **rasas** — se a lista contiver outras listas dentro, essas listas internas ainda são compartilhadas.

---

##  List Comprehension

Forma compacta e elegante de criar listas:

```python
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
```

Equivale a um loop `for` com `.append()`, mas em uma linha.

---

## Testes e Debugging

**Testes** — verificar se o código faz o que deveria. Tipos principais: testes de unidade (função por função) e testes de integração (o sistema todo).

**Debugging** — encontrar e corrigir erros. Estratégias úteis: `print()` em pontos chave, isolar o problema, testar casos extremos (lista vazia, número negativo, zero).

---

##  Exceções e Assertions

**Exceções** — erros que ocorrem durante a execução. Você pode capturá-los em vez de deixar o programa travar:

```python
try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Isso não é um número!")
```

**Assertions** — verificações que travam o programa imediatamente se uma condição não for verdadeira. Úteis para garantir que o programa está em um estado válido:

```python
assert x > 0, "x deve ser positivo"
```

---

## Dicionários

Estrutura de dados que mapeia **chaves** para **valores**. Diferente de listas, o acesso é por chave, não por índice:

```python
d = {'nome': 'Alice', 'idade': 25}
d['cidade'] = 'SP'     # adiciona
print(d['nome'])       # 'Alice'
```

Operações úteis: `.keys()`, `.values()`, `.items()`, `.get()`. Busca em dicionário é O(1) — muito mais rápida que busca em lista.

---

##  Recursão

Recursão é quando uma função chama a si mesma. Todo algoritmo recursivo tem dois componentes obrigatórios:

**Caso base** — condição que para a recursão. Sem ele, o programa trava em loop infinito.

**Caso recursivo** — a função resolve uma versão menor do problema e chama a si mesma.

```python
def fatorial(n):
    if n == 0:              # caso base
        return 1
    return n * fatorial(n - 1)  # caso recursivo
```

Comparando com loops iterativos, recursão é mais elegante para problemas que têm estrutura naturalmente recursiva, mas usa mais memória (cada chamada ocupa espaço na pilha).

---

##  Recursão em Não-Numéricos

Recursão funciona muito bem em estruturas como strings, listas e árvores:

```python
def inverte(s):
    if len(s) == 0:
        return ""
    return inverte(s[1:]) + s[0]
```

A ideia é sempre a mesma: resolver o problema para uma versão menor e combinar com o resultado atual.

---

##  Classes em Python

Classes permitem criar seus próprios tipos de dados, agrupando dados (**atributos**) e comportamentos (**métodos**):

```python
class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def falar(self):
        return f"{self.nome} faz {self.som}"

gato = Animal("Gato", "miau")
print(gato.falar())  # Gato faz miau
```

`__init__` é o construtor — roda automaticamente quando o objeto é criado. `self` representa a instância atual do objeto.

---

##  Métodos Especiais de Classes

Python tem métodos especiais (com `__`) que permitem que suas classes se comportem como tipos nativos:

```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"      # como print() exibe o objeto

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)  # soma com +
```

**Herança** — uma classe filha herda atributos e métodos da classe pai, podendo sobrescrever o que precisar:

```python
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "au")  # chama o construtor do pai
```

---

##  Herança

Herança permite que uma classe filha reutilize e estenda o comportamento de uma classe pai. É um dos pilares da programação orientada a objetos.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "..."

class Cachorro(Animal):
    def falar(self):           # sobrescreve o método do pai
        return "Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

dog = Cachorro("Rex")
print(dog.falar())  # Au!
```

**`super()`** — chama o método da classe pai, evitando repetição de código:

```python
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # aproveita o __init__ do pai
        self.raca = raca
```

Conceitos importantes:
- **Substituição (override)** — a classe filha redefine um método do pai
- **Herança múltipla** — Python permite herdar de mais de uma classe
- **Polimorfismo** — objetos de classes diferentes respondem ao mesmo método de formas diferentes

---

## Exemplo Prático: Fitness Tracker com OOP

Um rastreador de fitness é um bom exemplo de programação orientada a objetos porque tem dados e comportamentos naturalmente agrupados:

```python
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []

    def registrar_treino(self, tipo, duracao, calorias):
        self.historico.append({
            'tipo': tipo,
            'duracao': duracao,
            'calorias': calorias
        })

    def total_calorias(self):
        return sum(t['calorias'] for t in self.historico)

class Corredor(Usuario):
    def __init__(self, nome, idade, pace):
        super().__init__(nome, idade)
        self.pace = pace  # minutos por km

    def calcular_distancia(self, duracao):
        return duracao / self.pace
```

A OOP organiza o código de forma que cada objeto sabe o que é e o que faz — tornando o programa mais fácil de manter e expandir.

---

## Medindo Tempo e Contando Operações

Antes de falar em complexidade teórica, podemos medir o desempenho real de um programa:

```python
import time

inicio = time.time()
# código a medir
fim = time.time()
print(f"Tempo: {fim - inicio:.4f} segundos")
```

Porém, medir tempo real tem problemas: depende do hardware, da carga do sistema e da linguagem. Por isso usamos **contagem de operações** — contar quantas vezes as operações fundamentais são executadas conforme `n` cresce.

---

##  Big O e Theta (Θ)

**Big O — O(f(n))** — limite superior. O algoritmo nunca cresce mais rápido que `f(n)`. É a notação mais usada na prática.

**Theta — Θ(f(n))** — limite exato. O algoritmo cresce exatamente como `f(n)`, tanto no melhor quanto no pior caso.

Regras para simplificar:
- Descarta constantes: `3n² + 5` → `O(n²)`
- Fica com o termo dominante: `n² + n` → `O(n²)`
- Soma de loops sequenciais: `O(n) + O(n)` → `O(n)`
- Loops aninhados: `O(n) × O(n)` → `O(n²)`

**Hierarquia de crescimento** (do mais lento ao mais rápido):

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

---

##  Classes de Complexidade — Exemplos

| Complexidade | Nome | Exemplo |
|---|---|---|
| O(1) | Constante | Acesso a índice de lista, acesso a dicionário |
| O(log n) | Logarítmico | Busca binária, bisseção |
| O(n) | Linear | Loop simples, busca linear |
| O(n log n) | Linear-logarítmico | Merge sort, Tim sort |
| O(n²) | Quadrático | Bubble sort, loops aninhados |
| O(n³) | Cúbico | Multiplicação de matrizes ingênua |
| O(2ⁿ) | Exponencial | Força bruta em subconjuntos |
| O(n!) | Fatorial | Permutações, problema do caixeiro viajante |

```python
# O(1) — constante
def primeiro(lista):
    return lista[0]

# O(n) — linear
def busca(lista, alvo):
    for item in lista:
        if item == alvo:
            return True
    return False

# O(n²) — quadrático
def tem_duplicata(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False
```

---

##  Algoritmos de Ordenação

### Bubble Sort — O(n²)
Compara pares adjacentes e troca se estiverem fora de ordem. Simples mas lento.

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
```

### Selection Sort — O(n²)
A cada passo, encontra o menor elemento e coloca na posição correta.

```python
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
```

### Merge Sort — O(n log n)
Divide a lista ao meio, ordena cada metade recursivamente e junta. Muito mais eficiente.

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    meio = len(lst) // 2
    esq = merge_sort(lst[:meio])
    dir = merge_sort(lst[meio:])
    return merge(esq, dir)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    return resultado + esq[i:] + dir[j:]
```

Python usa internamente o **Tim Sort** (híbrido de merge sort e insertion sort) — O(n log n).

---

##  Plotagem de Gráficos

Python tem a biblioteca `matplotlib` para visualizar dados:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, label='y = x²')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Crescimento Quadrático')
plt.legend()
plt.show()
```

Tipos comuns de gráfico:
- `plt.plot()` — linha
- `plt.bar()` — barras
- `plt.scatter()` — dispersão
- `plt.hist()` — histograma

Útil para visualizar crescimento de algoritmos, comparar complexidades e analisar dados.

---

##  Acesso a Listas e Hashing

**Acesso a listas** — acessar `lista[i]` é sempre O(1) porque listas em Python são arrays contíguos na memória.

**Hashing** — técnica que converte uma chave em um índice numérico, permitindo acesso O(1). É o que faz dicionários e sets serem tão rápidos.

```python
# dicionário usa hashing internamente
d = {'chave': 'valor'}
print(d['chave'])  # O(1) — muito mais rápido que busca em lista
```

Colisões — quando duas chaves geram o mesmo hash — são tratadas internamente pelo Python.

---

##  Simulações

Simulações usam aleatoriedade para modelar sistemas complexos. Muito usadas em ciência, finanças e jogos:

```python
import random

def simular_lancamentos(n):
    resultados = {'cara': 0, 'coroa': 0}
    for _ in range(n):
        if random.random() < 0.5:
            resultados['cara'] += 1
        else:
            resultados['coroa'] += 1
    return resultados

print(simular_lancamentos(10000))
```

Com simulações podemos estimar probabilidades, comportamentos emergentes e fenômenos que são difíceis de calcular analiticamente.

