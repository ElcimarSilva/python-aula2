#4 - Faça um programa que receba um valor que é o valor pago, um segundo valor que
#é o preço do produto e retorne o troco a ser dado. (modifique para receber um valor de
#desconto e subtraia do valor do produto)
class MinhaClasse():
    def Subtracao(self):
        n1=int(input("Digite o valor que o cliente lhe entregou:"))
        n2 = int(input("Digite o valor produto:"))
        print('O troco é de ',n1-n2)

exemploObj = MinhaClasse()

exemploObj.Subtracao()
