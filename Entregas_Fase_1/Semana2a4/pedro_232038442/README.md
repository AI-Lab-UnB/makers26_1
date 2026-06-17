# Entregas da Fase 1 – Semanas 2 a 4

Este repositório reúne os exercícios das Semanas 2 a 4 do curso **MIT 6.100L – Introduction to CS and Programming Using Python**, divididos entre Finger Exercises e Problem Sets.

---

### Finger Exercises

São 26 scripts curtos, feitos logo após o estudo de cada tópico, enquanto o conceito ainda estava fresco. Passaram por fundamentos de Python, controle de fluxo, coleções de dados, funções, recursão, orientação a objetos e uma introdução à análise de complexidade com notação Big O.

---

### Problem Sets

Os Problem Sets foram outra história. Cada um exigiu integrar vários conceitos ao mesmo tempo para construir algo que realmente funcionasse de ponta a ponta.

- **PS0 e PS1:** Ponto de partida. Configuração do ambiente, cálculos matemáticos e os primeiros algoritmos iterativos, como simulações de poupança e pagamento de dívidas.

- **PS2 – Hangman:** Implementação completa do jogo da Forca. O desafio principal foi menos a lógica do jogo em si e mais garantir que as entradas do usuário fossem validadas e que a mecânica de turnos ficasse limpa e previsível.

- **PS3 – Document Distance:** Um algoritmo que calcula a similaridade entre dois textos usando distância de cossenos. Envolveu pré-processar strings, montar dicionários de frequência e aplicar fórmula matemática sobre estruturas de dados reais.

- **PS4 – Criptografia:** Sistema de criptografia baseado na Cifra de César, com quebra de senha por verificação cruzada contra um dicionário de palavras em inglês. Foi o primeiro contato sério com POO, herança e encapsulamento num contexto não trivial.

- **PS5 – Processamento de Imagens:** Manipulação direta de pixels em matrizes bidimensionais para filtrar e revelar imagens. Obrigou a pensar em como dados visuais são organizados na memória antes de conseguir fazer qualquer coisa com eles.

---

### Processo

A curva foi íngreme. Em poucas semanas o nível saltou de "declare uma variável" para "projete um sistema orientado a objetos com casos de teste". Cada Problem Set vinha acompanhado de uma bateria de testes (`test_ps*_student.py`) que funcionaram como árbitro objetivo do que estava funcionando ou não, o que na prática forçou um fluxo próximo ao TDD: código modular, funções bem definidas e nada de gambiarras escondidas.