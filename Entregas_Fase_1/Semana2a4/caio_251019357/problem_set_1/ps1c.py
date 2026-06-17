## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
deposito_inical = float(input("Digite seu deposito inical : "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


valor_entrada = 800000 * 0.25

r = 1.0

valor_economizado = deposito_inical * (1 + r/12)**36

maior = 1.0
menor = 0.0


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

if deposito_inical >= valor_entrada or deposito_inical >= (valor_entrada-100) :
    print("r = 0\n0 iterações")

elif (valor_economizado - 100) < valor_entrada:
    print("None")

else:

    count = 0
    # medio = (maior+menor)/2

    while(valor_economizado < ( valor_entrada - 100 ) or valor_economizado > (valor_entrada + 100) ):

        medio = (maior+menor)/2

        valor_economizado = deposito_inical * (1 + medio/12)**36

        if valor_economizado < (valor_entrada+100):

            menor = medio

            count+= 1

        else:

            maior = medio
            count += 1

    print(f"Taxa = {medio}")
    print(f"iterações = {count}")