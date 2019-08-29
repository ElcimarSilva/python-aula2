#15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles.
lista = []
menor10 = 0
while menor10 <10:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print("Numero repetido!!")
    else:
        menor10=menor10+1
        lista.append(valor)
maior = max(lista)
print (maior) # Falta Mostrar bonitinho

