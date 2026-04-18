def dot_product(v1, v2):
    if len(v1) != len(v2):
        print("Vectors must be of the same length");
        return None;
    return sum(x * y for x, y in zip(v1, v2)); #  basicamente, neste contexto, o zip() ele pega o primeiro elemento
                                               #  de cada lista e, então, monta pares (1, 4), depois o segundo (2, 5)
                                               #  e o terceiro (3, 6); multiplica cada par (4, 10, 18) e, por fim,
                                               #  soma os resultados para obter o produto escalar. (32)

Ta = (1, 2, 3);
Tb = (4, 5, 6);
print(dot_product(Ta, Tb)); # print 32
