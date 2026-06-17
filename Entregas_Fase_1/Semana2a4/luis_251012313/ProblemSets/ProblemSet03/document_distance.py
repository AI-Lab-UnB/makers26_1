# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Luis Gustavo Ferreira Nunes
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import os
import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split() # retorna uma lista de palavras, onde cada palavra é um elemento da lista.
                              # onde split() é um método de string que divide a string em uma lista de palavras usando espaços como delimitadores.


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    return_dict = {} # o dicionário de retorno irá armazenar a frequência de cada elemento (letra ou palavra) presente no input_iterable, 
                     # onde as chaves são os elementos e os valores são as frequências correspondentes
    for element in input_iterable: 
        if element in return_dict: # se o elemento já estiver no dicionário de retorno, incrementa a frequência do elemento em 1
            return_dict[element] += 1
        else:                      # se o elemento não estiver no dicionário de retorno, adiciona o elemento ao dicionário com uma frequência inicial de 1
            return_dict[element] = 1
    return return_dict # retorna o dicionário de frequências, onde as chaves são os elementos (letras ou palavras) e os valores são as frequências correspondentes
                       # o dicionário é construído iterando sobre cada elemento do input_iterable e contando quantas vezes cada elemento aparece, armazenando essa
                       # contagem no dicionário de retorno. Ou seja, o dicionário de retorno é uma representação da frequência de cada elemento no input_iterable.


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return get_frequencies(list(word)) # retorna um dicionário de frequências de letras em uma palavra,
                                       # onde get_frequencies é chamada com uma lista de caracteres da palavra (obtida usando list(word)),
                                       # e o dicionário resultante tem as letras como chaves e suas frequências como valores.


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    return round(1 - (calculate_difference(freq_dict1, freq_dict2) / calculate_total(freq_dict1, freq_dict2)), 2)
    # Calcula a pontuação de similaridade entre dois dicionários de frequências usando a fórmula dada,
    # onde calculate_difference basicamente calcula a diff total entre as frequências dos dois dicionários, 
    # e calculate_total calcula o total de frequências em ambos os dicionários. 
    
    # Serve para medir o quão semelhantes são os dois dicionários de frequências, 
    # com uma pontuação de 1 indicando que os dicionários são idênticos 
    # e uma pontuação de 0 indicando que os dicionários são completamente diferentes. 
    # A função retorna a pontuação de similaridade arredondada para 2 casas decimais.

def calculate_difference(freq_dict1, freq_dict2):
    diff = 0
    for key in freq_dict1: # itera sobre todas as chaves do primeiro dicionário
        if key in freq_dict2:
            diff += abs(freq_dict1[key] - freq_dict2[key]) # se a chave também estiver no segundo dicionário, calcula a diferença absoluta entre as frequências e adiciona ao diff
        else:
            diff += freq_dict1[key] # se a chave não estiver no segundo dicionário, adiciona a frequência do primeiro dicionário ao diff
    for key in freq_dict2: # itera sobre todas as chaves do segundo dicionário
        if key not in freq_dict1:
            diff += freq_dict2[key] # se a chave não estiver no primeiro dicionário, adiciona a frequência do segundo dicionário ao diff
    return diff # retorna a diferença total entre as frequências dos dois dicionários

def calculate_total(freq_dict1, freq_dict2):
    total = 0
    for key in freq_dict1: # itera sobre todas as chaves do primeiro dicionário
        total += freq_dict1[key] # obtem a frequência da chave e adiciona ao total
    for key in freq_dict2: # itera sobre todas as chaves do segundo dicionário
        total += freq_dict2[key] # obtem a frequência da chave e adiciona ao total
    return total # retorna o total de frequências

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    return_dict = {} # o dicionário de retorno irá armazenar a frequência combinada de cada palavra presente nos dois dicionários de entrada
    for key in freq_dict1: # itera sobre todas as chaves do primeiro dicionário
        if key in return_dict:
            return_dict[key] += freq_dict1[key] # se a chave já estiver no dicionário de retorno 
                                                # (ou seja, já foi adicionada a partir do segundo dicionário), 
                                                # adiciona a frequência do primeiro dicionário à frequência existente no dicionário de retorno
        else:
            return_dict[key] = freq_dict1[key] # se a chave não estiver no dicionário de retorno, adiciona a chave
                                               # e a frequencia do primeiro dicionário ao dicionário de retorno
    
    for key in freq_dict2: # itera sobre todas as chaves do segundo dicionário
        if key in return_dict:
            return_dict[key] += freq_dict2[key] # se a chave já estiver no dicionário de retorno (ou seja, já foi adicionada a partir do primeiro dicionário),
                                                # adiciona a frequência do segundo dicionário à frequência existente no dicionário de retorno
        else:
            return_dict[key] = freq_dict2[key] # o inverso do caso anterior: se a chave não estiver no dicionário de retorno, 
                                               # adiciona a chave e a frequencia do segundo dicionário ao dicionário de retorno.

    max_freq = max(return_dict.values()) # obtém a frequência máxima entre todas as palavras
    
    return sorted([key for key in return_dict if return_dict[key] == max_freq]) # retorna uma lista ordenada alfabeticamente das palavras que têm a frequência máxima


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    return_dict = {}
    word_list = text_to_list(load_file(file_path))
    word_freq = get_frequencies(word_list)
    total_words = len(word_list)
    for word in word_freq:
        return_dict[word] = word_freq[word] / total_words # calcula o TF para cada palavra usando a fórmula dada, 
                                                          # onde word_freq[word] é o número de vezes que a palavra aparece no documento 
                                                          # e total_words é o número total de palavras no documento

                                                          # o TF é uma medida da frequência de uma palavra em um doc,
                                                          # sendo basicamente o numero de vezes que a palavra aparece dividido pelo número total de palavras no documento.
                                                          # serve para normalizar a frequência de uma palavra em relação ao tamanho do documento, 
                                                          # permitindo comparações mais justas entre palavras em documentos de diferentes tamanhos.
    return return_dict

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    return_dict = {}
    total_docs = len(file_paths)
    for file_path in file_paths:
        word_freq = get_frequencies(text_to_list(load_file(file_path)))
        for word in word_freq:
            if word in return_dict:
                return_dict[word] += 1
            else:
                return_dict[word] = 1
    
    for word in return_dict:
        return_dict[word] = math.log10(total_docs / return_dict[word]) # calcula o IDF para cada palavra usando a fórmula dada, 
                                                                       # onde total_docs é o número total de documentos e return_dict[word] 
                                                                       # é o número de documentos que contêm a palavra

                                                                       # o IDF é uma medida da importância de uma palavra em um conjunto de documentos,
                                                                       # sendo calculado como o logaritmo do número total de documentos dividido pelo número de documentos que contêm a palavra. 
                                                                       # O IDF é usado para reduzir a importância de palavras que aparecem em muitos documentos,
                                                                       # pois essas palavras tendem a ser menos informativas para distinguir entre os documentos.
    
    return return_dict

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    return sorted([(word, tf * get_idf(idf_file_paths)[word]) for word, tf in get_tf(tf_file_path).items()], key=lambda x: (x[1], x[0])) 
    # retorna uma lista ordenada de tuplas (palavra, TF-IDF), onde o TF-IDF é calculado multiplicando o TF da palavra (obtido usando get_tf) 
    # pelo IDF da palavra (obtido usando get_idf). A lista é ordenada primeiro pelo valor do TF-IDF e, em caso de empate, pela ordem alfabética da palavra.


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    print(f"{"Test Problem 0: Prep Data":=^50}")

    base_dir = os.path.dirname(__file__)
    test_directory = os.path.join(base_dir, "tests/student_tests/")

    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']


    ## Tests Problem 1: Get Frequencies
    print(f"{"Test Problem 1: Get Frequencies":=^50}")

    test_directory = os.path.join(base_dir, "tests/student_tests/")

    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}


    ## Tests Problem 2: Get Letter Frequencies
    print(f"{"Test Problem 2: Get Letter Frequencies":=^50}")

    freq1 = get_letter_frequencies('hello')
    freq2 = get_letter_frequencies('that')
    print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    print(f"{"Test Problem 3: Similarity":=^50}")
    
    test_directory = os.path.join(base_dir, "tests/student_tests/")
   
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    word1_freq = get_letter_frequencies('toes')
    word2_freq = get_letter_frequencies('that')
    word3_freq = get_frequencies('nah')
    word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity1)       # should print 1.0
    print(word_similarity2)       # should print 0.25
    print(word_similarity3)       # should print 0.0
    print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    print(f"{"Test Problem 4: Most Frequent Word(s)":=^50}")

    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    print(f"{"Test Problem 5: Find TF-IDF":=^50}")

    tf_text_file = os.path.join(base_dir, 'tests/student_tests/hello_world.txt')
    idf_text_files = [os.path.join(base_dir, 'tests/student_tests/hello_world.txt'), os.path.join(base_dir, 'tests/student_tests/hello_friends.txt')]
    
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]