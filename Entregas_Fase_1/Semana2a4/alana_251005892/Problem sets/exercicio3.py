import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    lista = input_text.split()
    return lista


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    d = {}
    for  word in input_iterable:
        if word in d:
            d[word] +=1
        else:
            d[word] = 1
    return d


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    all_keys = set(freq_dict1.keys()) | set(freq_dict2.keys())
    diff = 0
    all = 0
    for elem in all_keys:
        if elem in freq_dict1 and elem in freq_dict2:
            diff += abs(freq_dict1[elem] - freq_dict2[elem])
        elif elem in freq_dict1 and elem not in freq_dict2:
            diff += freq_dict1[elem]
        elif elem in freq_dict2 and elem not in freq_dict1:
            diff += freq_dict2[elem]
    for eleme in all_keys:
        if eleme in freq_dict1 and eleme not in freq_dict2:
            all += freq_dict1[eleme] 
        elif eleme in freq_dict2 and eleme not in freq_dict1:
            all += freq_dict2[eleme]
        else:
            all += freq_dict2[eleme] + freq_dict1[eleme]
    return round(1- diff/all, 2)


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    dic= {}
    lista = []
    for u in freq_dict1:
        dic[u] = freq_dict1[u]
    for j in freq_dict2:
        if j in dic:
            dic[j] = dic[j] + freq_dict2[j]
        else:
            dic[j] = freq_dict2[j]
    
    maior_valor = max(dic.values())
    for k, v in dic.items():
        if v == maior_valor:
            lista.append(k)
    lista.sort()
    return lista
        
    
### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    texto = load_file(file_path)
    lista_palavra = text_to_list(texto)
    total = len(lista_palavra)
    frequencias = get_frequencies(lista_palavra)
    tf_dict = {}
    for palavra in frequencias:
        tf = frequencias[palavra]/total
        tf_dict[palavra] = tf
    return tf_dict

def get_idf(file_paths):
    total = len(file_paths)
    contagem_doc = {}
    for arquivo in file_paths:
        texto = load_file(arquivo)
        lista_palavras = set(text_to_list(texto))
        for i in lista_palavras:
            contagem_doc[i]= contagem_doc.get(i, 0) + 1
    idf_dic = {}
    for k, v in contagem_doc.items():
        idf = math.log10(total/ v )
        idf_dic[k] = idf
    return idf_dic


def get_tfidf(tf_file_path, idf_file_paths):
    lista = []
    dic_tf = get_tf(tf_file_path)
    dic_idf = get_idf(idf_file_paths)
    for palavra, k in dic_tf.items():
        tfidf = dic_tf[palavra] * dic_idf[palavra]
        lista.append((tfidf,palavra))
    lista.sort()
    lista_invertida = [(palavra, tfidf) for tfidf, palavra in lista]
    return lista_invertida
    


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    freq1 = get_letter_frequencies('hello')
    freq2 = get_letter_frequencies('that')
    print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    test_directory = "tests/student_tests/"
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
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    tf_text_file = 'tests/student_tests/hello_world.txt'
    idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]