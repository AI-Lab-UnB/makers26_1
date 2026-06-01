
# Problem Set 2, hangman.py
# Name: Gabriel
# Collaborators: None
# Time Spent:

import random
import string

WORDLIST_FILENAME = 'words.txt'

def load_words():
    print('Loading word list from file...')
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(len(wordlist), 'words loaded.')
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

# 1.1 - VERIFICA SE O JOGADOR GANHOU
# percorre cada letra da palavra secreta e checa se todas foram chutadas
def has_player_won(secret_word, letters_guessed):
    for letra in secret_word:
        if letra not in letters_guessed:
            return False
    return True

# 1.2 - MOSTRA O PROGRESSO DA PALAVRA
# monta a palavra com * nos lugares ainda nao descobertos
def get_word_progress(secret_word, letters_guessed):
    resultado = ''
    for letra in secret_word:
        if letra in letters_guessed:
            resultado += letra
        else:
            resultado += '*'
    return resultado

# 1.3 - RETORNA LETRAS DISPONIVEIS
# percorre o alfabeto e retorna as letras que ainda nao foram chutadas
def get_available_letters(letters_guessed):
    disponiveis = ''
    for letra in string.ascii_lowercase:
        if letra not in letters_guessed:
            disponiveis += letra
    return disponiveis

# FUNCAO AUXILIAR PARA O MODO AJUDA
# escolhe uma letra da palavra secreta que ainda nao foi revelada
def escolher_letra_para_revelar(secret_word, available_letters):
    choose_from = ''
    for letra in secret_word:
        if letra in available_letters and letra not in choose_from:
            choose_from += letra
    if len(choose_from) == 0:
        return None
    new = random.randint(0, len(choose_from) - 1)
    return choose_from[new]

# FUNCAO PRINCIPAL DO JOGO
# recebe a palavra secreta e o booleano with_help
# roda o loop ate o jogador ganhar ou perder
def hangman(secret_word, with_help):
    print('Welcome to Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')

    # criando as variaveis e armazenando os valores iniciais
    letras_chutadas = []
    chutes_restantes = 10
    vogais = 'aeiou'

    # fazendo loop ate o jogador ganhar ou ficar sem chutes
    while True:
        print('--------------')

        # verifica condicao de vitoria
        if has_player_won(secret_word, letras_chutadas):
            print('Congratulations, you won!')
            letras_unicas = len(set(secret_word))
            pontuacao = (chutes_restantes + 4 * letras_unicas) + (3 * len(secret_word))
            print('Your total score for this game is:', pontuacao)
            break

        # verifica condicao de derrota
        if chutes_restantes <= 0:
            print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
            break

        print('You have', chutes_restantes, 'guesses left.')
        print('Available letters:', get_available_letters(letras_chutadas))

        chute = input('Please guess a letter: ').lower()

        # modo ajuda com ! - revela uma letra ao custo de 3 chutes
        if with_help and chute == '!':
            if chutes_restantes < 3:
                print('Oops! Not enough guesses left:', get_word_progress(secret_word, letras_chutadas))
            else:
                letra_revelada = escolher_letra_para_revelar(secret_word, get_available_letters(letras_chutadas))
                if letra_revelada:
                    letras_chutadas.append(letra_revelada)
                    chutes_restantes -= 3
                    print('Letter revealed:', letra_revelada)
                    print(get_word_progress(secret_word, letras_chutadas))
            continue

        # entrada invalida - nao e letra ou tem mais de 1 caractere
        if not chute.isalpha() or len(chute) != 1:
            print('Oops! That is not a valid letter. Please input a letter from the alphabet:', get_word_progress(secret_word, letras_chutadas))
            continue

        # letra ja chutada anteriormente - nao perde chute
        if chute in letras_chutadas:
            print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letras_chutadas))
            continue

        # letra valida e nova - adiciona a lista de chutadas
        letras_chutadas.append(chute)

        # letra esta na palavra - nao perde chute
        if chute in secret_word:
            print('Good guess:', get_word_progress(secret_word, letras_chutadas))
        else:
            # letra nao esta na palavra - perde 2 se vogal, 1 se consoante
            print('Oops! That letter is not in my word:', get_word_progress(secret_word, letras_chutadas))
            if chute in vogais:
                chutes_restantes -= 2
            else:
                chutes_restantes -= 1

if __name__ == '__main__':
    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)