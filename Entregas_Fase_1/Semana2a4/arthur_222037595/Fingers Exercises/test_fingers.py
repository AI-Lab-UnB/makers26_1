# testes dos finger exercises - lectures 1 a 10
# roda com: python3 test_fingers.py

import io
import sys
import importlib.util


def rodar_script(arquivo, variaveis):
    with open(arquivo) as f:
        codigo = f.read()
    saida = io.StringIO()
    sys.stdout = saida
    exec(compile(codigo, arquivo, 'exec'), variaveis)
    sys.stdout = sys.__stdout__
    return saida.getvalue().strip()


def importar(arquivo):
    spec = importlib.util.spec_from_file_location("modulo", arquivo)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


passaram = 0
falharam = 0

def checar(descricao, obtido, esperado):
    global passaram, falharam
    if obtido == esperado:
        print(f"  ok  {descricao}")
        passaram += 1
    else:
        print(f"  FALHOU  {descricao}")
        print(f"    esperado: {repr(esperado)}")
        print(f"    obtido:   {repr(obtido)}")
        falharam += 1


print("\ntestando ex01 - (a+b)*c")
checar("caso simples (2+3)*4",  rodar_script("ex01.py", {"a":2, "b":3, "c":4}),  "20")
checar("com zero (0+5)*10",     rodar_script("ex01.py", {"a":0, "b":5, "c":10}), "50")
checar("tudo 1 (1+1)*1",        rodar_script("ex01.py", {"a":1, "b":1, "c":1}),  "2")

print("\ntestando ex02 - positivo, negativo ou zero")
checar("numero positivo",  rodar_script("ex02.py", {"number":  5}), "positive")
checar("numero negativo",  rodar_script("ex02.py", {"number": -3}), "negative")
checar("zero",             rodar_script("ex02.py", {"number":  0}), "zero")

print("\ntestando ex03 - hello world N vezes")
checar("N=3", rodar_script("ex03.py", {"N": 3}), "hello world\nhello world\nhello world")
checar("N=1", rodar_script("ex03.py", {"N": 1}), "hello world")
checar("N=0", rodar_script("ex03.py", {"N": 0}), "")

print("\ntestando ex04 - raiz cubica")
checar("27 -> 3",     rodar_script("ex04.py", {"N": 27}), "3")
checar("8 -> 2",      rodar_script("ex04.py", {"N": 8}),  "2")
checar("1 -> 1",      rodar_script("ex04.py", {"N": 1}),  "1")
checar("10 -> error", rodar_script("ex04.py", {"N": 10}), "error")
checar("2 -> error",  rodar_script("ex04.py", {"N": 2}),  "error")

print("\ntestando ex05 - indices pares")
checar('"abcdefg" vira "aceg"', rodar_script("ex05.py", {"my_str": "abcdefg"}), "aceg")
checar('"abcd" vira "ac"',      rodar_script("ex05.py", {"my_str": "abcd"}),    "ac")
checar('"a" vira "a"',          rodar_script("ex05.py", {"my_str": "a"}),       "a")
checar('"python" vira "pto"',   rodar_script("ex05.py", {"my_str": "python"}),  "pto")

print("\ntestando ex06 - busca binaria")
def answer_ex06(N):
    saida = rodar_script("ex06.py", {"N": N})
    for linha in saida.split("\n"):
        if linha.startswith("answer:"):
            return linha.split(":")[1].strip()

checar("achou N=0",    answer_ex06(0),    "0")
checar("achou N=500",  answer_ex06(500),  "500")
checar("achou N=1000", answer_ex06(1000), "1000")
checar("achou N=742",  answer_ex06(742),  "742")

print("\ntestando ex07 - equacao quadratica")
ex07 = importar("ex07.py")
checar("eval(1,1,1,1) = 3",  ex07.eval_quadratic(1, 1, 1, 1), 3)
checar("eval(2,0,0,3) = 18", ex07.eval_quadratic(2, 0, 0, 3), 18)
checar("eval(1,0,-1,1) = 0", ex07.eval_quadratic(1, 0, -1, 1), 0)

saida_two = io.StringIO()
sys.stdout = saida_two
ex07.two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)
sys.stdout = sys.__stdout__
checar("two_quadratics imprime 6", saida_two.getvalue().strip(), "6")

print("\ntestando ex08 - same_chars")
ex08 = importar("ex08.py")
checar('"abc" e "cab" -> True',     ex08.same_chars("abc", "cab"),     True)
checar('"abccc" e "caaab" -> True', ex08.same_chars("abccc", "caaab"), True)
checar('"abcd" e "cabaa" -> False', ex08.same_chars("abcd", "cabaa"),  False)
checar('"abcabc" e "cabz" -> False',ex08.same_chars("abcabc", "cabz"), False)

print("\ntestando ex09 - dot product")
ex09 = importar("ex09.py")
checar("(1,2,3)·(4,5,6) = (3,32)", ex09.dot_product((1,2,3),(4,5,6)), (3, 32))
checar("(1,0)·(0,1) = (2,0)",      ex09.dot_product((1,0),(0,1)),     (2, 0))
checar("(3,)·(3,) = (1,9)",        ex09.dot_product((3,),(3,)),       (1, 9))

print("\ntestando ex10 - all_true")
ex10 = importar("ex10.py")
par      = lambda n: n % 2 == 0
positivo = lambda n: n > 0
maior10  = lambda n: n > 10

checar("4 com [par, positivo] -> True",       ex10.all_true(4,  [par, positivo]),          True)
checar("3 com [par, positivo] -> False",      ex10.all_true(3,  [par, positivo]),          False)
checar("-2 com [par, positivo] -> False",     ex10.all_true(-2, [par, positivo]),          False)
checar("12 com [par, positivo, >10] -> True", ex10.all_true(12, [par, positivo, maior10]), True)
checar("8 com [par, positivo, >10] -> False", ex10.all_true(8,  [par, positivo, maior10]), False)
checar("lista vazia sempre True",             ex10.all_true(5,  []),                       True)

print(f"\n{passaram + falharam} testes no total: {passaram} passaram, {falharam} falharam\n")
