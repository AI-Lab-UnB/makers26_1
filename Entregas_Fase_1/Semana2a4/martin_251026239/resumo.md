# MIT 6.100L - Introduction to CS and Programming Using Python

Este repositório contém as soluções para os Problem Sets (PS0 a PS5) e Finger Exercises do curso MIT 6.100L (Fall 2022). O objetivo principal deste documento é registrar o progresso e os conceitos de programação em Python aprendidos durante a resolução de cada módulo.

## 🛠️ Ambiente de Desenvolvimento e Contexto
Embora eu já possuísse uma base nos fundamentos de Python, utilizei a densidade dos *Problem Sets* do MIT para consolidar esses conhecimentos e focar na resolução de problemas mais complexos.

Além disso, adaptei o fluxo de trabalho sugerido pelo curso:
* **Recomendação do MIT:** Anaconda e Spyder IDE.
* **Meu Setup:** Todo o desenvolvimento, execução e testes foram realizados utilizando o **Visual Studio Code (VS Code)** e a instalação padrão do Python, permitindo um fluxo mais ágil e integrado com o controle de versão (Git).

---

## Finger Exercises
Foram desenvolvidos 26 scripts curtos, cada um com um objetivo prático e bem definido. Eles serviram para fixar imediatamente os conceitos abordados em aula, englobando desde fundamentos básicos, controle de fluxo e estruturas de dados, até o uso de funções em Python.

---

## Problem Set 1: Compound Interest
Este projeto envolveu o uso de estruturas de repetição e algoritmos de busca para modelar a economia necessária para a compra de uma casa, considerando juros compostos e aumentos salariais. 

A fórmula principal de juros compostos aplicada foi:
$$amount\_saved = initial\_deposit \times (1 + \frac{r}{12})^{months}$$

**Aprendizados Principais:**
* **Controle de Fluxo:** Utilização de laços `while` e declarações `if/elif/else` para simular o acúmulo de capital mês a mês.
* **Busca Binária (Bisection Search):** Implementação de um algoritmo de busca logarítmica para encontrar a taxa de retorno ideal ($r$) capaz de atingir uma meta financeira em exatamente 36 meses.
* **Depuração e Rastreamento de Estado:** Gerenciamento do estado de múltiplas variáveis (salário, poupança, meses) ao longo de iterações contínuas.

---

## Problem Set 2: Hangman
O desenvolvimento do clássico jogo da forca ("Hangman") com a adição de um sistema de ajuda inteligente.

**Aprendizados Principais:**
* **Decomposição de Funções:** Quebra de um problema grande (o jogo inteiro) em funções auxiliares menores e testáveis (verificar vitória, revelar letras, obter letras disponíveis).
* **Manipulação de Strings e Listas:** Validação de entradas do usuário, higienização de dados (`str.lower()`, `str.isalpha()`) e iteração sobre caracteres.
* **Design de Interação:** Manutenção de um loop principal de jogo que gerencia o estado das vidas do jogador, penalidades diferenciadas para vogais e consoantes, e atualizações de interface no terminal.

---

## Problem Set 3: Document Distance
Um projeto focado em Recuperação da Informação, comparando a similaridade entre textos e músicas através da frequência de palavras e cálculos de TF-IDF (Term Frequency - Inverse Document Frequency).

O cálculo de similaridade baseou-se nas diferenças absolutas $\delta(e)$ e nas somas de frequências $\sigma(e)$ dos elementos. Também implementamos as seguintes métricas de relevância:

$$TF(w) = \frac{\text{frequência da palavra } w \text{ no documento}}{\text{total de palavras no documento}}$$

$$IDF(w) = \log_{10}\left(\frac{\text{total de documentos}}{\text{documentos contendo a palavra } w}\right)$$

$$TF-IDF(w) = TF(w) \times IDF(w)$$

**Aprendizados Principais:**
* **Dicionários (Hash Maps):** Mapeamento eficiente de palavras para suas respectivas frequências, lidando com contagens e chaves dinâmicas.
* **Processamento de Arquivos:** Leitura e conversão de arquivos de texto brutos em estruturas de dados manipuláveis (listas e strings).
* **Tradução de Fórmulas Matemáticas para Código:** Conversão de lógicas de somatório e logaritmos em funções Python puras.

---

## Problem Set 4: Recursion and Caesar Cipher
Este conjunto de problemas foi dividido em duas áreas fundamentais da computação: estruturas de dados em árvore (via recursão) e criptografia utilizando Programação Orientada a Objetos.

**Aprendizados Principais:**
* **Pensamento Recursivo:** Implementação de funções com casos base e casos recursivos para encontrar a altura de uma árvore e validar propriedades de *Heaps* (Max/Min Heaps).
* **Programação Orientada a Objetos (POO):** Criação de classes pai (`Message`) e classes filhas (`PlaintextMessage`, `EncryptedMessage`), utilizando herança e sobrescrita de métodos.
* **Criptografia e Tabela ASCII:** Manipulação de caracteres diretamente por seus valores numéricos usando `ord()` e `chr()` para criar e reverter cifras baseadas em *One Time Pads* através do operador módulo (`%`).

---

## Problem Set 5: Using Libraries
O projeto final explorou o processamento de imagens e a esteganografia (ocultação de imagens dentro de outras imagens) manipulando pixels através da biblioteca PIL (Python Imaging Library).

**Aprendizados Principais:**
* **Uso de Bibliotecas Externas:** Leitura de documentação técnica para aplicar métodos de uma biblioteca que não foi escrita pelo próprio programador.
* **Matrizes e Tuplas:** Representação de cores RGB como tuplas e transformação de imagens através de multiplicação de matrizes para simular daltonismo.
* **Operações Binárias e Módulo:** Extração dos Bits Menos Significativos (LSB) de valores inteiros na base 10 (0-255) para revelar imagens secretas escondidas nos canais de cores, sem a necessidade de converter explicitamente os números para strings binárias.

---

## Considerações Finais sobre os Problem Sets
Diferente dos Finger Exercises, os Problem Sets apresentaram um escopo de contexto bem maior, exigindo a integração de múltiplos conceitos simultaneamente para construir as soluções, sendo bem mais desafiadores.