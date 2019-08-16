#7 - Escreva um algoritmo que leia 10 números informados pelo usuário e,
#depois, informe o
#menor número
#o maior número
#a soma dos números informados e a

#média aritmética dos números informados.

class DezNumeros():
    numero = 0
    numeros = []
    media = 0
    menor = 0
    maior = 0
    def entrada_numeros(self):
        for i in range(4):
            self.numero = float(input("Digite os numeros a serem calculados: "))
            self.numeros.append(self.numero)

    def calculo_media(self):
        self.media= sum(self.numeros)/(len(self.numeros))#len puxa a quantidade de valores que tem dentro da lista
        print ("A media dos 10 numeros é{}".format(self.media))

    def calculo_maior_numero(self):
        aux= self.numeros[0]
        for i in range (len(self.numeros)):
            if self.numeros [i] > aux:
                aux=self.numeros[i]
        self.maior=aux

        #self.maior = max(self.numeros)
        print("o Maior dos 10 numeros é{}".format(self.maior))
    def calculo_menor_numero(self):
        aux = self.numeros[0]
        for i in range(len(self.numeros)):
            if self.numeros[i] < aux:
                aux = self.numeros[i]
        self.menor = aux

        #self.menor = min(self.numeros)
        print("o Menor dos 10 numeros é{}".format(self.menor))

    #def calculo_soma(self):

chama=DezNumeros()

'''
while True:
    opcao=int(input('1-Informe os 10 numeros: \n'
                    '2-Calcule a média aritmética\n'

                    '0-Sair'))
    if opcao ==1:
       chama.entrada_numeros()
    elif opcao ==2:
       chama.calculo_media()
    elif opcao ==0:
        exit()
    else:
        print("Opção Invalida")

'''

foo = DezNumeros()
foo.entrada_numeros()
foo.calculo_media()
foo.calculo_maior_numero()
foo.calculo_menor_numero()