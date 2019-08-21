#2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo,
#e mostre-o por extenso. Este número deverá variar entre 1 e 5. Se o usuário introduzir
#um número que não pertença a este intervalo, mostre a frase “número inválido”.

cont= ('zero','um','dois','três','quatro',        #Tupla
'cinco','seis','sete','oito','nove','dez','onze','doze',
'treze','quatorze ou catorze','quinze',
'dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    numero = int(input('Digite um numero entre 1 e 5: '))
    if 1 <= numero <= 5:
        break
    print ('Opção invalida, tente novamente\n', end='')
print(f'voce digitou o numero {cont[numero]}') # Mostra o valor da tupla formatado



