

'''
ps1b: CALCULAR QUANTOS MESES LEVA PARA ECONOMIZAR O VALOR DE ENTRADA DE UMA CASA
COM AUMENTO SALARIAL SEMESTRAL
'''
# criando as variáveis e armazenando os valores do usuário
salario_anual = float(input("Salário anual: "))
Mensal_economia = float(input("Quanto você economiza por mês (Ex 0.10): "))
casa_sonho = float(input("Valor da casa dos sonhos: "))
aumento_semestral = float(input("Aumento semestral (Ex 0.07): "))

entrada = casa_sonho * 0.25
salario_mensal = salario_anual / 12
economizar = salario_mensal * Mensal_economia
valor_economia = 0
meses = 0

# loop até chegar no valor da entrada da casa
while valor_economia < entrada:
    valor_economia += economizar
    valor_economia += valor_economia * (0.05 / 12)
    meses += 1

    # a cada 6 meses, aumenta o salário
    if meses % 6 == 0:
        salario_anual += salario_anual * aumento_semestral
        salario_mensal = salario_anual / 12
        economizar = salario_mensal * Mensal_economia

print("Meses necessários para economizar a entrada: ", meses)
