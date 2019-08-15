#2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo,
#e mostre-o por extenso. Este número deverá variar entre 1 e 5. Se o usuário introduzir
#um número que não pertença a este intervalo, mostre a frase “número inválido”.
class MediaAluno():
    def maiorMedia(self):
        nota1 = int(input("Nota 1: "))
        nota2 = int(input("Nota 2: "))
        nota3 = int(input("Nota 3: "))
        media = ((nota1 + nota2 + nota3) / 3)  # Calculo de media

        # Verifica se maior que 18 "Aprovado"
        if media >= 18:
            print("Aprovado")
        else:
            print("Menor que 18")

chama=MediaAluno()

while True:
    opcao=int(input('1-Para começar a inserir suas notas \n'
                    '0-Sair'
                    ))
    if opcao ==1:
        chama.maiorMedia()
    elif opcao ==0:
        exit()
    else:
        print("Opção Invalida")
