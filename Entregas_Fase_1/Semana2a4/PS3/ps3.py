'''
Preparar os dados:
text_to_list: transforma o texto em lista de palavras
get_frequencies: conta quantas vezes cada palavra aparece
get_letter_frequencies: faz o mesmo mas para letras de uma palavra

Calcular similaridade
calculate_similarity_score: compara dois dicionários e retorna um número de 0 a 1
get_most_frequent_words: junta dois dicionários e retorna as palavras mais frequentes

Calcular TF-IDF :
get_tf: frequência de cada palavra no documento
get_idf: o quão rara cada palavra é entre todos os documentos
get_tfidf: multiplica TF × IDF e retorna ordenado

'''

import math
import string

# FUNCAO FORNECIDA - NAO MODIFICAR
# carrega o arquivo e remove pontuacao
def load_file(filename):
    inFile = open(filename, 'r')
    text = inFile.read()
    inFile.close()
    for char in string.punctuation:
        text = text.replace(char, '')
    return text.lower()

# PROBLEMA 0 - TEXTO PARA LISTA
# transforma a string em uma lista de palavras
def text_to_list(input_text):
    return input_text.split()

# PROBLEMA 1 - FREQUENCIA DAS PALAVRAS
# cria um dicionario com cada palavra e quantas vezes ela aparece
def get_frequencies(input_iterable):
    frequencias = {}
    for elemento in input_iterable:
        if elemento in frequencias:
            frequencias[elemento] += 1
        else:
            frequencias[elemento] = 1
    return frequencias

# PROBLEMA 2 - FREQUENCIA DAS LETRAS
# reutiliza get_frequencies para contar letras de uma palavra
def get_letter_frequencies(word):
    return get_frequencies(word)

# PROBLEMA 3 - CALCULO DE SIMILARIDADE
# calcula o score de similaridade entre dois dicionarios de frequencia
# score entre 0 (completamente diferentes) e 1 (identicos)
def calculate_similarity_score(freq_dict1, freq_dict2):
    # cria o conjunto de todas as palavras unicas dos dois dicionarios
    todas_palavras = set(freq_dict1.keys()) | set(freq_dict2.keys())

    soma_delta = 0
    soma_sigma = 0

    for palavra in todas_palavras:
        count1 = freq_dict1.get(palavra, 0)
        count2 = freq_dict2.get(palavra, 0)

        # delta = diferenca absoluta entre as frequencias
        delta = abs(count1 - count2)
        # sigma = soma das frequencias
        sigma = count1 + count2

        soma_delta += delta
        soma_sigma += sigma

    # similaridade = 1 - (soma_delta / soma_sigma)
    similaridade = 1 - (soma_delta / soma_sigma)
    return round(similaridade, 2)

# PROBLEMA 4 - PALAVRAS MAIS FREQUENTES
# retorna lista com as palavras mais frequentes combinando dois dicionarios
# se houver empate retorna lista ordenada alfabeticamente
def get_most_frequent_words(freq_dict1, freq_dict2):
    # combina as frequencias dos dois dicionarios
    combinado = {}
    for palavra in freq_dict1:
        combinado[palavra] = combinado.get(palavra, 0) + freq_dict1[palavra]
    for palavra in freq_dict2:
        combinado[palavra] = combinado.get(palavra, 0) + freq_dict2[palavra]

    # encontra a maior frequencia
    maior_freq = max(combinado.values())

    # retorna todas as palavras com a maior frequencia em ordem alfabetica
    resultado = []
    for palavra in combinado:
        if combinado[palavra] == maior_freq:
            resultado.append(palavra)
    return sorted(resultado)

# PROBLEMA 5 - TF (TERM FREQUENCY)
# calcula a frequencia de cada palavra em relacao ao total de palavras do arquivo
def get_tf(text_file):
    texto = load_file(text_file)
    palavras = text_to_list(texto)
    frequencias = get_frequencies(palavras)
    total_palavras = len(palavras)

    tf = {}
    for palavra in frequencias:
        tf[palavra] = frequencias[palavra] / total_palavras
    return tf

# PROBLEMA 5 - IDF (INVERSE DOCUMENT FREQUENCY)
# calcula o quanto cada palavra e rara entre todos os documentos
def get_idf(text_files):
    total_documentos = len(text_files)

    # conta em quantos documentos cada palavra aparece
    documentos_por_palavra = {}
    for arquivo in text_files:
        texto = load_file(arquivo)
        palavras = set(text_to_list(texto))
        for palavra in palavras:
            documentos_por_palavra[palavra] = documentos_por_palavra.get(palavra, 0) + 1

    # calcula o idf de cada palavra
    idf = {}
    for palavra in documentos_por_palavra:
        idf[palavra] = math.log10(total_documentos / documentos_por_palavra[palavra])
    return idf

# PROBLEMA 5 - TF-IDF
# combina TF e IDF e retorna lista ordenada de tuplas (palavra, tfidf)
def get_tfidf(text_file, text_files):
    tf = get_tf(text_file)
    idf = get_idf(text_files)

    tfidf = []
    for palavra in tf:
        valor = tf[palavra] * idf.get(palavra, 0)
        tfidf.append((palavra, valor))

    # ordena por valor tfidf crescente, em caso de empate ordena alfabeticamente
    tfidf.sort(key=lambda x: (x[1], x[0]))
    return tfidf


if __name__ == "__main__":
    test_directory = "tests/student_tests/"

    hello_world = load_file(test_directory + 'hello_world.txt')
    hello_friend = load_file(test_directory + 'hello_friends.txt')
    world = text_to_list(hello_world)
    friend = text_to_list(hello_friend)

    # problema 0
    print(world)   # ['hello', 'world', 'hello']
    print(friend)  # ['hello', 'friends']

    # problema 1
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)   # {'hello': 2, 'world': 1}
    print(friend_word_freq)  # {'hello': 1, 'friends': 1}

    # problema 2
    print(get_letter_frequencies('hello'))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(get_letter_frequencies('that'))   # {'t': 2, 'h': 1, 'a': 1}

    # problema 3
    word1_freq = get_letter_frequencies('toes')
    word2_freq = get_letter_frequencies('that')
    print(calculate_similarity_score(word1_freq, word1_freq))      # 1.0
    print(calculate_similarity_score(word1_freq, word2_freq))      # 0.25
    print(calculate_similarity_score(world_word_freq, friend_word_freq))  # 0.4

    # problema 4
    freq_dict1 = {"hello": 5, "world": 1}
    freq_dict2 = {"hello": 1, "world": 5}
    print(get_most_frequent_words(freq_dict1, freq_dict2))  # ['hello', 'world']

    # problema 5
    tf_text_file = test_directory + 'hello_world.txt'
    idf_text_files = [test_directory + 'hello_world.txt', test_directory + 'hello_friends.txt']
    print(get_tf(tf_text_file))
    print(get_idf(idf_text_files))
    print(get_tfidf(tf_text_file, idf_text_files))