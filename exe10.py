#10 - receba três notas de um aluno e informe se ele passou ou reprovou.

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))
media = (nota1+nota2+nota3)/3

if media >= 6:
    print(f"Aluno Aprovado!! {media:.2f}")
else:
    print(f"Aluno Reprovado!!{media:.2f}")
