import math

def load_file(filename):
    with open(filename, 'r') as f:
        text = f.read().lower()
    for char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(char, '')
    return text

# Problema 0: texto para lista
def text_to_list(text):
    return text.split()

# Problema 1: frequência de palavras
def get_frequencies(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Problema 2: frequência de letras 
def get_letter_frequencies(word):
    return get_frequencies(list(word))

# Problema 3: similaridade
def calculate_similarity_score(freq1, freq2):
    unique = set(freq1.keys()) | set(freq2.keys())
    total_delta = 0
    total_sigma = 0
    for word in unique:
        count1 = freq1.get(word, 0)
        count2 = freq2.get(word, 0)
        total_delta += abs(count1 - count2)
        total_sigma += count1 + count2
    if total_sigma == 0:
        return 1.0
    return round(1 - total_delta / total_sigma, 2)

# Problema 4: palavras mais frequentes
def get_most_frequent_words(freq1, freq2):
    combined = {}
    for word, count in freq1.items():
        combined[word] = combined.get(word, 0) + count
    for word, count in freq2.items():
        combined[word] = combined.get(word, 0) + count
    max_freq = max(combined.values())
    return sorted([word for word, count in combined.items() if count == max_freq])

# Problema 5a
def get_tf(text_file):
    words = text_to_list(load_file(text_file))
    total = len(words)
    freq = get_frequencies(words)
    return {word: count / total for word, count in freq.items()}

# Problema 5b
def get_idf(text_files):
    total_docs = len(text_files)
    word_doc_count = {}
    for file in text_files:
        words = set(text_to_list(load_file(file)))
        for word in words:
            word_doc_count[word] = word_doc_count.get(word, 0) + 1
    return {word: math.log10(total_docs / count) for word, count in word_doc_count.items()}

# Problema 5c
def get_tfidf(text_file, text_files):
    tf = get_tf(text_file)
    idf = get_idf(text_files)
    tfidf = {word: tf_val * idf.get(word, 0) for word, tf_val in tf.items()}
    return sorted(tfidf.items(), key=lambda x: (x[1], x[0]))


if __name__ == "__main__":
    text1 = "hello world hello"
    text2 = "hello friends"

    world = text_to_list(text1)
    friend = text_to_list(text2)
    print(world)  
    print(friend)  

    world_freq = get_frequencies(world)
    friend_freq = get_frequencies(friend)
    print(world_freq)  
    print(friend_freq)  

    print(get_letter_frequencies('hello'))  
    print(get_letter_frequencies('that'))   

    print(calculate_similarity_score(get_letter_frequencies('toes'), get_letter_frequencies('toes')))  
    print(calculate_similarity_score(get_letter_frequencies('toes'), get_letter_frequencies('that'))) 
    print(calculate_similarity_score(get_letter_frequencies('toes'), get_frequencies('nah')))          
    print(calculate_similarity_score(world_freq, friend_freq))                                         

    print(get_most_frequent_words({"hello": 5, "world": 1}, {"hello": 1, "world": 5}))  