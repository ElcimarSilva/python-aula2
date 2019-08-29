#13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens
#serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais
#velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.

homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))
mulher1 = int(input("Digite a idade da primeira mulher: "))
mulher2 = int(input("Digite a idade da segunda mulher: "))
homemOld = 0
homemYoung = 0
mulherOld = 0
mulherYoung = 0

if homem1 > homem2:
    homemOld=homem1
    homemYoung=homem2
else:
    homemOld=homem2
    homemYoung=homem1

if mulher1 > mulher2:
    mulherOld=mulher1
    mulherYoung=mulher2
else:
    mulherOld=mulher2
    mulherYoung=mulher1


print("A soma do homem mais velho com a mulher mais novaé :",homemOld+mulherYoung)
print("A multiplicação do homem mais velho com a mulher mais nova: ",homemYoung*mulherOld)
