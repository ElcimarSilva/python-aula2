#3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração,
#multiplicação e divisão). O usuário deve informar dois números e o programa deve
#fazer as quatro operações. (modifique para calcular tudo no mesmo método, somando
#1 ao resultado de cada operação)

class MinhaClasse():
    def Soma(self):
        n1=int(input("Digite o primeiro valor:"))
        n2 = int(input("Digite o segundo valor:"))
        print(n1+n2)

    def Subtracao(self):
        n1=int(input("Digite o primeiro valor:"))
        n2 = int(input("Digite o segundo valor:"))
        print(n1-n2)

    def Multiplicacao(self):
        n1 = int(input("Digite o primeiro valor:"))
        n2 = int(input("Digite o segundo valor:"))
        print(n1 * n2)

    def Divisao(self):
        n1 = int(input("Digite o primeiro valor:"))
        n2 = int(input("Digite o segundo valor:"))
        print(n1 / n2)


exemploObj = MinhaClasse()
while True:
    opcao=int(input('1-Soma\n'
                    '2-Subtração\n'
                    '3-Multiplicação\n'
                    '4-Divisão\n'
                    '0-Sair'))
    if opcao ==1:
        exemploObj.Soma()
    elif opcao ==2:
        exemploObj.Subtracao()
    elif opcao ==3:
        exemploObj.Multiplicacao()
    elif opcao ==4:
        exemploObj.Divisao()
    elif opcao ==0:
        exit()
    else:
        print("Opção Invalida")
