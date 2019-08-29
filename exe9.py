#9 - faça um método que receba um número X e uma palavra no console e repita x vezes a essa frase.

numero = int(input("Digite o numero de vezes a ser repetida a palavra: "))
palavra = input("Digite a palavra a ser repetida: ")
def meu_metodo():
    for i in range(numero):
        print ("Estou repetindo a palavra: ",palavra)
meu_metodo()