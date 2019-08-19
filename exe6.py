#6 - Faça um algoritmo que leia um nº inteiro e mostre uma
#mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo

numero=int(input("Digite o numero a ser verificado: "))
num_par= numero%2
if num_par==0:
    print ('o numero {} é par '.format(numero))
elif num_par!=0:
    print('o numero {} é impar '.format(numero))


