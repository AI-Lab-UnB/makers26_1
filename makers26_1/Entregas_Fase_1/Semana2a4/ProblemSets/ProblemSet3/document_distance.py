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
    words = input_text.split()
    return words

### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):

    frequencies={}

    for name in input_iterable:
        if name in frequencies:
            frequencies[name]+=1
        else:
            frequencies[name]=1
    
    return frequencies

### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    
    letters = {}

    for char in word:
        if char in letters:
            letters[char]+=1
        else:
            letters[char]=1

    return letters

### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    
    phi = {}
    sigma={}

    for word in freq_dict1:
        if word in freq_dict2:
            phi[word] = abs(freq_dict1[word]-freq_dict2[word])
            sigma[word]=freq_dict1[word]+freq_dict2[word]
        else:
            phi[word] = abs(freq_dict1[word]-0)
            sigma[word]=freq_dict1[word]
    
    for word in freq_dict2:
        if word not in freq_dict1:
            phi[word] = abs(freq_dict2[word]-0)
            sigma[word]=freq_dict2[word]

    divided=0
    divisor=0
    for word in phi:
        divided+=phi[word]
        divisor+=sigma[word]

    if divisor==0:
        return 1;

    return round(float(1 - (divided / divisor)), 2)

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    
    combined_freq = {}

    for word in freq_dict1:
        combined_freq[word] = freq_dict1[word]

    for word in freq_dict2:

        if word not in combined_freq:
            combined_freq[word]=freq_dict2[word]
        else:
            combined_freq[word]+=freq_dict2[word]

    sorted_keys = sorted(combined_freq, key=combined_freq.get, reverse=True)

    if not sorted_keys:
        return []

    words = []
    max_value = combined_freq[sorted_keys[0]]

    for word in sorted_keys:
        if combined_freq[word] == max_value:
            words.append(word)
        else:
            break
    
    words.sort()
    return words


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    words=text_to_list(load_file(file_path))
    counts=get_frequencies(words)

    total_words=len(words)
    tf_dict={}
    
    for word in counts:
        tf_dict[word]=counts[word]/total_words
    return tf_dict

def get_idf(file_paths):
    num_docs = len(file_paths)
    word_doc_counts = {}
    
    for path in file_paths:
        words = text_to_list(load_file(path))
        unique_words = set(words) 
        
        for word in unique_words:
            word_doc_counts[word] = word_doc_counts.get(word, 0) + 1
            
    idf_dict = {}
    for word, count in word_doc_counts.items():
        idf_dict[word] = math.log10(num_docs / count)
        
    return idf_dict

def get_tfidf(tf_file_path, idf_file_paths):
    tf = get_tf(tf_file_path)
    idf = get_idf(idf_file_paths)
    
    tfidf_list = []
    
    for word in tf:
        score = tf[word] * idf.get(word, 0)
        tfidf_list.append((word, score))
    
  
    tfidf_list.sort(key=lambda x: (x[1], x[0]))
    return tfidf_list


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