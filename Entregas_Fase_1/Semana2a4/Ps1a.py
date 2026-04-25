'''
ps1a: CALCULCULAR QUANTOS MESES LEVA PARA ECONOMIZAR O VALOR DE ENTRADA DE UMA CASA
ENTRADA FLOAT 
SALARIO ANUAL
PORCENTAGEM A ECONOMIZAR
VALOR DA CASA DOS SONHOS
quanto voce pode economizar por mes
REGRAS
VALOR DE ENTRADA = 0.25
VALOR ECONOMICO INCIAL = 0
R = 0.05
valor de economia *(R/12)
valor economizado pelos meses eu terei a entrada da casa em quantos meses
'''
#criando as variaveis e armazeando os valores do usuário
salario_anual = float(input("Salário anual: "))
Mensal_economia = float(input("Quanto você economiza por mês (Ex (0.10)?"))
casa_sonho = float(input("Valor da casa dos sonhos: "))
entrada = casa_sonho * 0.25
salario_mensal = salario_anual / 12
economizar = salario_mensal * Mensal_economia
valor_economia = 0
meses = 0   
#fazendo loop ate chegar o valor da entrada da casa
while valor_economia < entrada:
        valor_economia += economizar
        valor_economia += valor_economia * (0.05/12)    
        meses += 1
print("Meses necessários para economizar a entrada: ", meses)


