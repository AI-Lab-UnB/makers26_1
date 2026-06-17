'''
ps1c: ENCONTRAR A MENOR TAXA DE RETORNO NECESSÁRIA PARA ATINGIR
O VALOR DE ENTRADA EM EXATAMENTE 36 MESES USANDO BUSCA BINÁRIA
'''

# entrada do usuário
deposito_inicial = float(input("Depósito inicial: "))

# constantes
custo_casa = 800000
entrada = custo_casa * 0.25  # 200000
meses_alvo = 36
margem = 100

# verificar se depósito inicial já é suficiente
if deposito_inicial >= entrada - margem:
    taxa = 0.0
    passos = 0
    print("Passos na busca binária: ", passos)
    print("Taxa de retorno: ", taxa)

# verificar se é impossível mesmo com 100% de retorno
else:
    # simular com 100% de retorno
    valor_economia = deposito_inicial
    for mes in range(meses_alvo):
        valor_economia += valor_economia * (1.0 / 12)

    if valor_economia < entrada - margem:
        taxa = None
        passos = 0
        print("Passos na busca binária: ", passos)
        print("Taxa de retorno: ", taxa)

    # busca binária
    else:
        taxa_baixa = 0.0
        taxa_alta = 1.0
        taxa = (taxa_baixa + taxa_alta) / 2
        passos = 0

        while True:
            # simular 36 meses com a taxa atual
            valor_economia = deposito_inicial
            for mes in range(meses_alvo):
                valor_economia += valor_economia * (taxa / 12)

            passos += 1

            # verificar se está dentro da margem
            if abs(valor_economia - entrada) < margem:
                break

            # ajustar busca binária
            elif valor_economia < entrada:
                taxa_baixa = taxa
            else:
                taxa_alta = taxa

            taxa = (taxa_baixa + taxa_alta) / 2

        print("Passos na busca binária: ", passos)
        print("Taxa de retorno: ", round(taxa, 10))
