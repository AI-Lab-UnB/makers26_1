# Curso
https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022

# Guia de Python para POO  
https://www.w3schools.com/python/python_oop.asp 

# Árvores 
### Como funciona:
https://youtu.be/K1a2Bk8NrYQ?si=e-w8ukdp_BV3DbcT

### Como atravessar:
https://youtu.be/WLvU5EQVZqY?si=pAu-WMfuUoJaBggV

# Heaps
### Como funciona:
https://youtu.be/AE5I0xACpZs?si=5QeYjTqqGdplkjft

# Listas 
### Como deletar ou apenas remover alguns itens
https://www.rocketseat.com.br/blog/artigos/post/como-remover-itens-listas-python

# Meus aprendizados dos psets

## Classes em Python & POO
- Classes são modelos (blueprints) para objetos com **atributos** (dados) e **métodos** (funções)  
- `__init__` inicializa os atributos do objeto
- `__init__` da classe pai deve rodar antes de você usar atributos definidos nele  
- **Herança**: uma classe filha (ex: `PlaintextMessage`) herda métodos de uma classe pai (ex: `Message`)  
- Chamar um método em um objeto (`obj.method()`) automaticamente passa o `obj` como `self`
- `method` vs `method()`: o primeiro é uma referência à função, o segundo realmente executa ela  
- Sempre armazene **cópias** de entradas mutáveis (ex: `self.pad = pad[:]`) para evitar que mudanças externas afetem seu objeto  

## Operações Binárias & Bitwise
- Números podem ser representados em binário (ex: `214 = 11010110`)  
- Para extrair os últimos `n` bits de um número: `number % 2**n`  
- Para limitar um valor ao intervalo `[32, 126]` (95 valores): `(value - 32 + shift) % 95 + 32`  
- `bin()` retorna uma string como `'0b1010'` — não é um número para fazer cálculos  
- `random.randint(a, b)` é **inclusivo** nos dois extremos, então `randint(0, 109)` retorna valores de `[0, 109]`  

## PIL (Python Imaging Library)
- `Image.open(filename)` — abre um arquivo de imagem  
- `img.getdata()` — retorna os pixels, `list()` converte para lista
- `img.size` — retorna `(largura, altura)` como propriedade (sem parênteses)  
- `img.mode` — retorna o modo da imagem (`'RGB'` ou `'L'` para escala de cinza)  
- `Image.new(mode, size)` — cria uma imagem em branco  
- `img.putdata(pixels_list)` — preenche a imagem com pixels (modifica diretamente, não retorna nada)  
- Pixels devem ser **inteiros ou tuplas** — floats causam `TypeError`  

## Como Imagens Funcionam
- **Imagens preto e branco (BW)**: cada pixel é um único inteiro (0–255)  
- **Imagens RGB**: cada pixel é uma tupla com 3 inteiros `(R, G, B)`, cada um de 0–255  
- **Esteganografia**: esconder dados nos bits menos significativos (LSBs) dos pixels  
- Para revelar uma imagem escondida: extraia os últimos `n` bits e depois escale para `[0, 255]`  
  - Para 1 bit: `value * 255`  
  - Para 3 bits: `int(value * 255/7)`  