# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math
from collections import Counter


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
    
    list = input_text.split()

    return list



### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    
    frequency = Counter(input_iterable)

    return dict(frequency)




### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    
    
    return get_frequencies(word)




### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    
    U = []
    frequency_differences = []
    frequency_totals = []


    for key in freq_dict1:

        if key not in U:
            U.append(key)

    for key in freq_dict2:
        
        if key not in U:
            U.append(key)


    for key in U:

        if key in freq_dict1:

            count_1 = freq_dict1[key]

        else:

            count_1 = 0

        if key in freq_dict2:

            count_2 = freq_dict2[key]

        else:

            count_2 = 0


        calculate_difference = abs(count_1 - count_2)
        frequency_differences.append(calculate_difference)

        calculate_totals = count_1 + count_2
        frequency_totals.append(calculate_totals)

    

    similarity = 1 - (sum(frequency_differences) / sum(frequency_totals))
    similarity_final = round(similarity, 2)

    return similarity_final





### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
   
    bigger = 0 
    most_frequents = []  

    for key in freq_dict1:
       
        if key in freq_dict2:
           
            sum = freq_dict1[key] + freq_dict2[key]

            if sum > bigger:
                bigger = sum
                most_frequents.clear()
                most_frequents.append(key)

            elif sum == bigger:
                most_frequents.append(key)

        else:

            if freq_dict1[key] > bigger:
                bigger = freq_dict1[key] 
                most_frequents.clear()
                most_frequents.append(key)

            elif freq_dict1[key] == bigger:
                most_frequents.append(key)

    

    for key in freq_dict2:
        
        if key not in freq_dict1:

            if freq_dict2[key] > bigger:
                bigger = freq_dict2[key]
                most_frequents.clear()
                most_frequents.append(key)

            elif freq_dict2[key] == bigger:
                most_frequents.append(key)


    return sorted(most_frequents)
             



### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    
    text = load_file(file_path)
    list_words = text_to_list(text)

    total_words = len(list_words)

    frequencies = get_frequencies(list_words)

    dict_tf = {}



    for key in frequencies:
        
        tf = frequencies[key]/total_words

        dict_tf[key] = tf

    return dict_tf




    
def get_idf(file_paths):

    total_paths = len(file_paths)
    dict_frequencies = {}
   


    for path in file_paths:

        text = load_file(path)
        list_words = text_to_list(text)

        list_aux = []


        for word in list_words:

            if word not in dict_frequencies:
                dict_frequencies[word] = 1
                list_aux.append(word)

            elif word in dict_frequencies and word not in list_aux :
                dict_frequencies[word] += 1
                list_aux.append(word)



    dict_idf = {}
    
    for key in dict_frequencies:

        idf = math.log10(total_paths/dict_frequencies[key])

        dict_idf[key] = idf

    
    return dict_idf
                

        


def get_tfidf(tf_file_path, idf_file_paths):
    
    dict_tf = get_tf(tf_file_path)
    dict_idf = get_idf(idf_file_paths)

    list_tf_idf = []



    for key in dict_tf:

        tf_idf = dict_tf[key] * dict_idf[key]

        new_tupla = (key, tf_idf)

        list_tf_idf.append(new_tupla)

    
    return sorted(list_tf_idf, key=lambda x: (x[1], x[0]))
    


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    # ## Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    # ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    # # Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    # # Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    # # Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    # Tests Problem 5: Find TF-IDF
    tf_text_file = 'tests/student_tests/hello_world.txt'
    idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]