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
    
    return input_text.split()


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    
    freq_dict = {}
    for item in input_iterable:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    
    all_keys = set(freq_dict1.keys()).union(set(freq_dict2.keys()))
    
    diff = 0
    total = 0
    
    for key in all_keys:
        freq1 = freq_dict1.get(key, 0)
        freq2 = freq_dict2.get(key, 0)
        
        diff += abs(freq1 - freq2)
        total += (freq1 + freq2)
        
    return round(1 - (diff / total), 2)


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    
    combined_freq = {}
    all_keys = set(freq_dict1.keys()).union(set(freq_dict2.keys()))
    
    for key in all_keys:
        combined_freq[key] = freq_dict1.get(key, 0) + freq_dict2.get(key, 0)
        
    max_freq = max(combined_freq.values())
    
    most_frequent = [word for word, freq in combined_freq.items() if freq == max_freq]
    
    return sorted(most_frequent)


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    
    text = load_file(file_path)
    words = text_to_list(text)
    frequencies = get_frequencies(words)
    total_words = len(words)
    
    tf_dict = {}
    for word, count in frequencies.items():
        tf_dict[word] = count / total_words
        
    return tf_dict

def get_idf(file_paths):

    total_docs = len(file_paths)
    words_in_docs = []
    all_unique_words = set()
    
    for path in file_paths:
        text = load_file(path)
        unique_words_in_doc = set(text_to_list(text))
        words_in_docs.append(unique_words_in_doc)
        all_unique_words.update(unique_words_in_doc)
        
    idf_dict = {}
    for word in all_unique_words:
        docs_with_word = sum(1 for doc in words_in_docs if word in doc)
        idf_dict[word] = math.log10(total_docs / docs_with_word)
        
    return idf_dict

def get_tfidf(tf_file_path, idf_file_paths):

    tf_dict = get_tf(tf_file_path)
    idf_dict = get_idf(idf_file_paths)
    
    tfidf_list = []
    
    for word, tf_val in tf_dict.items():
        idf_val = idf_dict.get(word, 0.0) 
        tfidf_val = tf_val * idf_val
        tfidf_list.append((word, tfidf_val))
        
    return sorted(tfidf_list, key=lambda x: (x[1], x[0]))


if __name__ == "__main__":
    
    ## Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
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
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
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