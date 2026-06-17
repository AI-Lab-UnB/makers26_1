import math

def text_to_list(text):
    return text.split()

def get_frequencies(lista):
    d = dict()
    for c in lista:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def get_letter_frequencies(palavra):
    return get_frequencies(palavra)

def calculate_similarity_score(dict1, dict2):
    chaves_unicas = set(dict1) | set(dict2)
    soma_diferencas = 0
    soma_totais = 0
    
    for chave in chaves_unicas:
        count1 = dict1.get(chave, 0)
        count2 = dict2.get(chave, 0)
        soma_diferencas += abs(count1 - count2)
        soma_totais += count1 + count2
        
    similaridade = 1 - (soma_diferencas / soma_totais)
    return round(similaridade, 2)

def get_most_frequent_words(dict1, dict2):
    frequencia_combinada = dict()
    
    for palavra, freq in dict1.items():
        frequencia_combinada[palavra] = freq
        
    for palavra, freq in dict2.items():
        if palavra in frequencia_combinada:
            frequencia_combinada[palavra] += freq
        else:
            frequencia_combinada[palavra] = freq
            
    max_freq = max(frequencia_combinada.values())
    
    palavras_frequentes = []
    for palavra, freq in frequencia_combinada.items():
        if freq == max_freq:
            palavras_frequentes.append(palavra)
            
    return sorted(palavras_frequentes)

def get_tf(text_file):
    carregar = load_file(text_file)
    transformar = get_frequencies(text_to_list(carregar))
    somar = sum(transformar.values())
    dicionario_tf = dict()
    for palavra, freq in transformar.items():
        dicionario_tf[palavra] = freq / somar
    return dicionario_tf

def get_idf(text_files):
    num_docs = len(text_files)
    contagem_docs = dict()
    
    for doc in text_files:
        carregar = load_file(doc)
        palavras = text_to_list(carregar)
        palavras_unicas = set(palavras)
        
        for palavra in palavras_unicas:
            if palavra in contagem_docs:
                contagem_docs[palavra] += 1
            else:
                contagem_docs[palavra] = 1
                
    dicionario_idf = dict()
    for palavra, freq in contagem_docs.items():
        dicionario_idf[palavra] = math.log10(num_docs / freq)
        
    return dicionario_idf

def get_tfidf(text_file, text_files):
    tf_dict = get_tf(text_file)
    idf_dict = get_idf(text_files)
    
    tfidf_list = []
    for palavra, tf_val in tf_dict.items():
        idf_val = idf_dict.get(palavra, 0.0)
        tfidf_list.append((palavra, tf_val * idf_val))
        
    return sorted(tfidf_list, key=lambda x: (x[1], x[0]))