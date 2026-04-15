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
    word_list = input_text.split()
    return word_list


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    frequency = {}
    for item in input_iterable:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency        
        

### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    listed_word = list(word)
    letter_frequency = {}
    for letter in listed_word:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    return letter_frequency


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    all_keys = set(freq_dict1.keys()) | set(freq_dict2.keys())
    
    diff_sum = 0
    total_sum = 0
    
    for key in all_keys:
        f1 = freq_dict1.get(key, 0)
        f2 = freq_dict2.get(key, 0)
        diff_sum += abs(f1 - f2)
        total_sum += f1 + f2
        
    if total_sum == 0:
        return 1.0
    
    res = 1 - (diff_sum / total_sum)
    return round(res, 2)


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    all_keys = set(freq_dict1.keys()) | set(freq_dict2.keys())
    
    combined_freqs = {}
    for word in all_keys:
        combined_freqs[word] = freq_dict1.get(word, 0) + freq_dict2.get(word, 0)
    
    if not combined_freqs:
        return []
    
    max_freq = max(combined_freqs.values())
    
    most_frequent = []
    for word in combined_freqs:
        if combined_freqs[word] == max_freq:
            most_frequent.append(word)

    most_frequent.sort()
    
    return most_frequent


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    file = load_file(file_path)
    text = text_to_list(file)
    freq = get_frequencies(text)

    qty_words = 0    
    for key in freq:
        qty_words += freq[key]
    
    new_dict = {}
    for word in freq:
        tf = freq[word] / qty_words
        new_dict[word] = tf
    
    return new_dict


def get_idf(file_paths):
    total_doc = len(file_paths)
    
    doc_counts = {}
    for file_path in file_paths:
        file = load_file(file_path)
        text = text_to_list(file)
        
        unique_words = set(text)
        for word in unique_words:
            doc_counts[word] = doc_counts.get(word, 0) + 1
        
    idf_dict = {}
    for word, count in doc_counts.keys():
        idf_dict[word] = math.log10(total_doc / count)

    return idf_dict
        
    
def get_tfidf(tf_file_path, idf_file_paths):
    tf = get_tf(tf_file_path)
    idf = get_idf(idf_file_paths)
    
    tfidf_list = []
    
    for word, tf_val in tf.items():
        idf_val = idf.get(word, 0)
        score = tf_val * idf_val
        tfidf_list.append((word, score))
        
    
    return tfidf_list
                



if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    test_directory = "Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_3/tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    test_directory = "Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_3/tests/student_tests/"
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
    test_directory = "Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_3/tests/student_tests/"
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

    # ## Tests Problem 4: Most Frequent Word(s)
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    tf_text_file = 'Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_3/tests/student_tests/hello_world.txt'
    idf_text_files = ['Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_3/tests/student_tests/hello_world.txt', 'Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_3/tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]
    