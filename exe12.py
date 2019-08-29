#12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    print(f"O valor maior é:{valor1}")
else:
    print("O valor maior é: ", valor2)