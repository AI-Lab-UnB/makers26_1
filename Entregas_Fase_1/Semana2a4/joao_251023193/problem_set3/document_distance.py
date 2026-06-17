# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

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

    #split() - divide the words by the space and append in a list
    return input_text.split()
    


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):

    frequency = {}
    for word in input_iterable:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
            
    return frequency



### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):

    frequency = {}
    for letter in word:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    
    return frequency



### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    
    #criando uma lista sem termos duplicados para armazenar as letras
    freq_list_both = list(freq_dict1.keys())
    freq_list_both += list(freq_dict2.keys())
    freq_list_both = set(freq_list_both)
    
    
    #calculating the frequency differences
    freq_difference = 0
    for letter in freq_list_both:
        if letter not in freq_dict1:
            freq_dict1[letter] = 0
        elif letter not in freq_dict2:
            freq_dict2[letter] = 0
            
        freq_difference += abs(freq_dict1[letter] - freq_dict2[letter])
        
        
    #calculating the frequency totals
    freq_totals = 0
    for letter in freq_list_both:
        if letter not in freq_dict1:
            freq_dict1[letter] = 0
        elif letter not in freq_dict2:
            freq_dict2[letter] = 0
            
        freq_totals += abs(freq_dict1[letter] + freq_dict2[letter])
        
        
    #calculating the similarity
    similarity = 1 - (freq_difference/freq_totals)
    
    return round(similarity, 2)



### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    
    #creating a common dict for both others dicts
    freq_dict_both = freq_dict1.copy()
    most_frequent_words = []
    
    for keys in freq_dict2:
        if keys not in freq_dict_both:
            freq_dict_both[keys] = 1
        else:
            freq_dict_both[keys] += 1
            
    #function that sort itens in descending order
    freq_dict_both = sorted(freq_dict_both.items(), key=lambda item: item[1], reverse = True)
    
    for key in freq_dict_both:
        most_frequent_words.append(key[0])
        
    return most_frequent_words



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
    
    tf_dict = {}
    all_words = 0
    
    #calculate the number of words and creating a frequency dictionary
    #putting the words in a list
    text = load_file(file_path)
    words_in_text = text_to_list(text)

    for word in words_in_text:
        all_words += 1
        
    get_frequencies(words_in_text)
    freq_dict = get_frequencies(words_in_text)
    
    
    #calculate the TF and add it in a dictionary with his respective word
    for word in freq_dict:
        tf = freq_dict[word] / all_words
        tf_dict[word] = tf
        
    return tf_dict

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
    
    total_paths = len(file_paths)
    
    
    num_files_dict = {}
    
    for file in file_paths:
        
        text = load_file(file)
        words_in_text = text_to_list(text)
        
        aux_list = []
        
        for word in words_in_text:
            
            if word not in num_files_dict:
                num_files_dict[word] = 1
                aux_list.append(word)
                
            elif word in num_files_dict and word not in aux_list:
                num_files_dict[word] += 1
            
            
    
    
    idf_final_dict = {}
    for word in num_files_dict:
        
        idf = math.log10(total_paths/num_files_dict[word])
        
        idf_final_dict[word] = idf
        
    return idf_final_dict
    

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
        
    tf_idf_list = []
    
    tf = get_tf(tf_file_path)
    idf = get_idf(idf_file_paths)
    
    for word in tf:
        tf_idf = (word, tf[word] * idf[word])
        tf_idf_list.append(tf_idf)
        
    return tf_idf_list
        
        
            
        
        
        
    pass


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
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

    ## Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]